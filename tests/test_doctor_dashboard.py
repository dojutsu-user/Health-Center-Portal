import pytest

from ddf import G

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from appointments.models import Appointment
from student.models import Student, VisitHistory
from doctor.models import Doctor


@pytest.mark.django_db
class TestDoctorDashboard:

    def _login(self, user, client):
        client.force_login(user)

    def test_doctor_dashboard_response(self, doctor, client):
        self._login(doctor.user, client)
        response = client.get('/doctor/dashboard/')
        assert response.status_code == 200, 'Response should be 200 OK for doctor dashboard'
        assert response.context_data['doctor'] == doctor, 'Doctor instance should be same as logged in user'

    def test_student_should_not_able_to_access_doc_dashboard(self, student, client):
        self._login(student.user, client)
        response = client.get('/doctor/dashboard/')
        assert response.status_code == 403, 'Student is not allowed to access doctor dashboard'

    def test_staff_should_not_be_able_to_access_doc_dashboard(self, client):
        user = G(User, is_staff=True)
        self._login(user, client)
        response = client.get('/doctor/dashboard/')
        assert response.status_code == 403, 'Staff members are not allowed to access doctor dashboard'

        client.logout()
        admin = G(User, is_staff=True, is_superuser=True)
        self._login(admin, client)
        response = client.get('/doctor/dashboard/')
        assert response.status_code == 403, 'Admin members are not allowed to access doctor dashboard'

    def test_doc_edit_profile_view_correct_form_submission(self, doctor, client):
        self._login(doctor.user, client)
        response = client.get(f'/doctor/dashboard/edit-profile/{doctor.pk}/')
        assert response.status_code == 200, 'Edit profile view should return 200 OK response for doctor'
        old_about_detail = doctor.about
        new_about_detail = 'new about details'

        form_data = {
            'name': doctor.name,
            'about': new_about_detail,
            'education': doctor.education,
            'available_description': doctor.available_description,
        }

        response = client.post(f'/doctor/dashboard/edit-profile/{doctor.pk}/', form_data)
        assert response.status_code == 302, 'Correct for submission should return redirect response'
        assert response.has_header('location') == True, 'Redirection url should be present in response header'
        assert response.get('location') == f'/doctor/dashboard/edit-profile/{doctor.pk}/', 'Location header must contain redirection url which is the edit profile page in this case'

        doctor.refresh_from_db()
        assert doctor.about == new_about_detail, 'About detail should get updated after correct form submission'

    def test_doc_edit_profile_view_incorrect_form_submission(self, doctor, client):
        self._login(doctor.user, client)
        response = client.get(f'/doctor/dashboard/edit-profile/{doctor.pk}/')
        assert response.status_code == 200, 'Edit profile view should return 200 OK response for doctor'

        old_about_detail = doctor.about
        new_about_detail = ''

        form_data = {
            'name': doctor.name,
            'about': new_about_detail,
            'education': doctor.education,
            'available_description': doctor.available_description,
        }

        response = client.post(f'/doctor/dashboard/edit-profile/{doctor.pk}/', form_data)
        form = response.context_data.get('form')
        assert form.is_valid() == False, 'Form should not be valid as it contains wrong data'
        
        errors = form.errors.as_data()
        assert errors.get('about') != None, 'Error for "about" field should be present in the form'
        assert errors['about'][0].message == 'This field is required.', 'Error about missing "about" field should be present in the form'

        doctor.refresh_from_db()
        assert doctor.about == old_about_detail, '"About" field should not get updated on wrong submission of form'

    def test_doctor_search_via_name(self, doctor, client):
        self._login(doctor.user, client)
        response = client.get('/doctor/dashboard/search/')
        assert response.status_code == 200, 'Search view should return 200 OK response for doctor'
        assert len(response.context_data.get('object_list')) == 0, 'There should not be any results without the query url param'

        user_1 = G(User, first_name='Dummy', last_name='Name')
        student_1 = G(Student, user=user_1)
        user_2 = G(User, first_name='Foo', last_name='Bar')
        student_2 = G(Student, user=user_2)

        # testing with first_name
        search_query = 'dummy'
        response = client.get(f'/doctor/dashboard/search/?q={search_query}')
        search_results = response.context_data.get('object_list')
        assert len(search_results) == 1, 'There should be exactly one result'
        assert search_results[0] == student_1, '"student_2" should be returned as only the search result'

        # testing with wrong query
        search_query = 'hello'
        response = client.get(f'/doctor/dashboard/search/?q={search_query}')
        search_results = response.context_data.get('object_list')
        assert len(search_results) == 0, 'There should  not any search result'

        # testing with last_name
        search_query = 'bar'
        response = client.get(f'/doctor/dashboard/search/?q={search_query}')
        search_results = response.context_data.get('object_list')
        assert len(search_results) == 1, 'There should be exactly one result'
        assert search_results[0] == student_2, '"student_2" should be returned as only the search result'

    def test_doctor_search_via_email(self, doctor, client):
        self._login(doctor.user, client)
        response = client.get('/doctor/dashboard/search/')
        assert response.status_code == 200, 'Search view should return 200 OK response for doctor'
        assert len(response.context_data.get('object_list')) == 0, 'There should not be any results without the query url param'

        user_1 = G(User, email='dummy@name.com')
        student_1 = G(Student, user=user_1)
        user_2 = G(User, email='foo@bar.com')
        student_2 = G(Student, user=user_2)

        # testing with only username
        search_query = 'dummy'
        response = client.get(f'/doctor/dashboard/search/?q={search_query}')
        search_results = response.context_data.get('object_list')
        assert len(search_results) == 1, 'There should be exactly one result'
        assert search_results[0] == student_1, '"student_2" should be returned as only the search result'

        # testing with domain
        search_query = 'bar.com'
        response = client.get(f'/doctor/dashboard/search/?q={search_query}')
        search_results = response.context_data.get('object_list')
        assert len(search_results) == 1, 'There should be exactly one result'
        assert search_results[0] == student_2, '"student_2" should be returned as only the search result'

        # testing with full email
        search_query = 'foo@bar.com'
        response = client.get(f'/doctor/dashboard/search/?q={search_query}')
        search_results = response.context_data.get('object_list')
        assert len(search_results) == 1, 'There should be exactly one result'
        assert search_results[0] == student_2, '"student_2" should be returned as only the search result'

    def test_doctor_dashboard_list_of_patient(self, doctor, client):
        self._login(doctor.user, client)
        response = client.get('/doctor/dashboard/list-of-patients/')
        assert response.status_code == 200, 'List of patients view should return 200 OK response for doctor'

        visit_histories = response.context_data['object_list']
        assert len(visit_histories) == 0, 'No visit histories are present.'

        # creating dummy students
        user_1 = G(User)
        student_1 = G(Student, user=user_1)
        user_2 = G(User)
        student_2 = G(Student, user=user_2)

        # creating dummy doctor
        user_3 = G(User)
        doctor_1 = G(Doctor, user=user_3)

        # creating visit histories
        vh_1 = G(VisitHistory, student=student_1, doctor=doctor)
        vh_2 = G(VisitHistory, student=student_2, doctor=doctor)
        vh_3 = G(VisitHistory, student=student_2, doctor=doctor_1)

        # testing
        response = client.get('/doctor/dashboard/list-of-patients/')
        visit_histories = response.context_data['object_list']
        assert len(visit_histories) == 2, 'There should be two visit histories the logged in doctor'

    def test_doctor_medicine_stock_information_page(self, doctor, client, create_medicines):
        self._login(doctor.user, client)
        response = client.get('/doctor/dashboard/medicines-stock/')
        assert response.status_code == 200, 'Doctor should be able to view medicine stock information'

        medicines = response.context_data.get('object_list')
        assert len(medicines) == 10, 'Ten medicines are there in total'

    def test_appointment_list_view_response(self, doctor, student, client):
        self._login(doctor.user, client)
        response = client.get('/doctor/dashboard/appointments/')
        assert response.status_code == 200, 'Doctor should be able to view all its appointments'
        assert len(response.context_data['object_list']) == 0, 'There are no appointments currently'

        # creating another dummy doctor
        user_1 = G(User)
        doctor_1 = G(Doctor, user=user_1)

        # creating appointments
        appointment_1 = G(Appointment, doctor=doctor, student=student)
        appointment_2 = G(Appointment, doctor=doctor_1, student=student)

        response = client.get('/doctor/dashboard/appointments/')
        assert len(response.context_data['object_list']) == 1, 'There are exactly one appointment for the logged in doctor'

    def test_doctor_dashboard_student_details(self, doctor, student, client):
        self._login(doctor.user, client)
        response = client.get(f'/doctor/dashboard/student-details/{student.pk}/')
        assert response.status_code == 200, 'Doctor should be able to view details on any student'
