from ddf import G

from django.utils import timezone

from appointments.forms import AppointmentCreateForm
from appointments.models import Appointment


class TestAppointmentCreationForm:

    def test_successfull_form_submission(self, doctor):
        datetime_of_appoint = timezone.now() + timezone.timedelta(days=1)
        datetime_of_appoint = timezone.datetime.strftime(
            datetime_of_appoint,
            '%m/%d/%Y %H:%M'
        )
        form_data = {
            'doctor': doctor.pk,
            'date_of_appointment': datetime_of_appoint,
        }

        form = AppointmentCreateForm(form_data)
        assert form.is_valid() == True, 'Form should be valid on correct data submission'

    def test_wrong_data_submission_form_submission(self, doctor):
        datetime_of_appoint = timezone.now() - timezone.timedelta(days=1)
        datetime_of_appoint = timezone.datetime.strftime(
            datetime_of_appoint,
            '%m/%d/%Y %H:%M'
        )
        form_data = {
            'doctor': doctor.pk,
            'date_of_appointment': datetime_of_appoint,
        }

        form = AppointmentCreateForm(form_data)
        assert form.is_valid() == False, 'Form should be valid on correct data submission'


class TestAppointmentCreationView:

    def _login(self, user, client):
        client.force_login(user)
    
    def test_form_successfull_submission(self, doctor, student, client):
        self._login(student.user, client)
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
        assert Appointment.objects.all().count() == 1, 'There is exactly one appointment object present in db'
        assert response.status_code == 302, 'Successfull form submission should return redirect response'
        assert response.get('location') == '/student/dashboard/all-appointments/', 'Redirection should be to the appointment list view'

    def test_form_wrong_data_submission(self, doctor, student, client):
        self._login(student.user, client)
        datetime_of_appoint = timezone.now() - timezone.timedelta(days=1)
        datetime_of_appoint = timezone.datetime.strftime(
            datetime_of_appoint,
            '%m/%d/%Y %H:%M'
        )
        form_data = {
            'doctor': doctor.pk,
            'date_of_appointment': datetime_of_appoint,
        }

        response = client.post('/student/dashboard/new-appointment/', form_data)
        assert Appointment.objects.all().count() == 0, 'There are no appointment objects present in db'
        assert response.status_code == 200, 'Unsuccessfull form submission should return to the same page'
        assert response.context_data['form'].is_valid() == False, 'Form should be invalid'
        
        errors = response.context_data['form'].errors.as_data()
        assert errors['date_of_appointment'][0].message == 'Please select the correct values of date and time.', 'Error about wrong value should be present in the form'


class TestAppointmentUpdateView:

    def _login(self, user, client):
        client.force_login(user)

    def test_appointment_cancelled(self, doctor, student, client):
        self._login(doctor.user, client)
        appointment = G(Appointment, student=student, doctor=doctor)
        response = client.get(f'/appointments/update/{appointment.pk}/cancel/')
        assert response.status_code == 302, 'Updation of appointment should return redirect response'
        assert response.get('location') == '/doctor/dashboard/appointments/', 'Updation of appointment should return to appointment list view of doctor'

        appointment.refresh_from_db()
        assert appointment.is_cancelled == True, 'Appointment should be cancelled'
        assert appointment.is_confirmed == False, 'Appointment should not be confirmed'

    def test_appointment_confirmed(self, doctor, student, client):
        self._login(doctor.user, client)
        appointment = G(Appointment, student=student, doctor=doctor)
        response = client.get(f'/appointments/update/{appointment.pk}/confirm/')
        assert response.status_code == 302, 'Updation of appointment should return redirect response'
        assert response.get('location') == '/doctor/dashboard/appointments/', 'Updation of appointment should return to appointment list view of doctor'

        appointment.refresh_from_db()
        assert appointment.is_cancelled == False, 'Appointment should be cancelled'
        assert appointment.is_confirmed == True, 'Appointment should not be confirmed'
