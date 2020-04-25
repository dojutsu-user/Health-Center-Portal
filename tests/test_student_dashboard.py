import pytest

from ddf import G

from django.contrib.auth.models import User
from django.utils import timezone

from appointments.models import Appointment
from student.models import VisitHistory, Student


@pytest.mark.django_db
class TestStudentDashboard:

    def _login(self, user, client):
        client.force_login(user)

    def test_stud_dashboard_response(self, student, client):
        self._login(student.user, client)
        response = client.get('/student/dashboard/')
        assert response.status_code == 200, 'Response should be 200 OK for student dashboard'
    
    def test_stud_dashboard_history(self, student, doctor, client):
        self._login(student.user, client)
        
        visit_1 = G(VisitHistory, student=student, doctor=doctor)
        visit_2 = G(VisitHistory, student=student, doctor=doctor)

        response = client.get('/student/dashboard/')
        assert response.status_code == 200, 'Response should be 200 OK for student dashboard'
        
        visits = response.context_data.get('visits')
        assert len(visits) == 2, 'Two Visits should be present in the context data'
        assert visits[0].doctor.pk == doctor.pk, 'Doctor pk should be the same as created.'
        assert visits[1].doctor.pk == doctor.pk, 'Doctor pk should be the same as created.'
    
    def test_doctor_should_not_able_to_access_stud_dashboard(self, doctor, client):
        self._login(doctor.user, client)
        response = client.get('/student/dashboard/')
        assert response.status_code == 403, 'Doctor is not allowed to access student dashboard'
    
    def test_staff_should_not_be_able_to_access_stud_dashboard(self, client):
        user = G(User, is_staff=True)
        self._login(user, client)
        response = client.get('/student/dashboard/')
        assert response.status_code == 403, 'Staff members are not allowed to access student dashboard'

        client.logout()
        admin = G(User, is_staff=True, is_superuser=True)
        self._login(admin, client)
        response = client.get('/student/dashboard/')
        assert response.status_code == 403, 'Admin members are not allowed to access student dashboard'

    def test_stud_medicine_stock_information_page(self, student, client, create_medicines):
        self._login(student.user, client)
        response = client.get('/student/dashboard/medicines-stock/')
        assert response.status_code == 200, 'Student should be able to view medicine stock information'

        medicines = response.context_data.get('medicines')
        assert len(medicines) == 10, 'Ten medicines are there in total'

    def test_create_appointment_page_response(self, student, client):
        self._login(student.user, client)
        response = client.get('/student/dashboard/new-appointment/')
        assert response.status_code == 200, 'Student should be able to view appointment create page'

    def test_appointments_list_page_response_with_no_appointments(self, student, client):
        self._login(student.user, client)
        response = client.get('/student/dashboard/all-appointments/')
        assert response.status_code == 200, 'Student should be able to view all appointments'
    
    def test_appointments_list_page_response_with_appointments(self, student, doctor, client):
        self._login(student.user, client)
        
        appointment_1 = G(Appointment, student=student, doctor=doctor)
        appointment_2 = G(Appointment, student=student, doctor=doctor)
        appointment_3 = G(Appointment, student=student, doctor=doctor)

        # creating appointment for another student
        user_1 =  G(User)
        student_1 = G(Student, user=user_1)
        appointment_4 = G(Appointment, student=student_1, doctor=doctor)

        response = client.get('/student/dashboard/all-appointments/')
        assert response.status_code == 200, 'Student should be able to view all appointments'

        appointments = response.context_data.get('object_list')
        assert len(appointments) == 3, 'Three appointments are made for the student'

    def test_create_appointment_redirects_to_appointments_list_page(self, student, doctor, client):
        self._login(student.user, client)
        response = client.get('/student/dashboard/new-appointment/')
        assert response.status_code == 200, 'Student should be able to view appointment create page'

        datetime_of_appoint = timezone.now() + timezone.timedelta(days=1)
        datetime_of_appoint = timezone.datetime.strftime(
            datetime_of_appoint,
            '%m/%d/%Y %H:%M'
        )
        form_data = {
            'doctor': doctor.pk,
            'date_of_appointment': datetime_of_appoint,
        }
        response = client.post('/student/dashboard/new-appointment/', form_data)
        assert response.url == '/student/dashboard/all-appointments/', 'Creation of a appointment should return to all appointments page'
