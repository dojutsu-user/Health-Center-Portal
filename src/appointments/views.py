"""Views for appointments app."""

import time

from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, CreateView
from django.urls import reverse_lazy

from appointments.forms import AppointmentCreateForm
from appointments.models import Appointment
from doctor.mixins import UserMustBeDoctorMixin
from doctor.models import Doctor
from student.mixins import UserMustBeStudentMixin
from student.models import Student


class AppointmentUpdateView(UserMustBeDoctorMixin, RedirectView):

    """
    Appointment update view for doctors.

    It is for confirmation/cancellation of the appointments.
    This view is to be only used by doctors.
    """

    http_method_names = ['get', 'post']

    def get_context_data(self):
        context = {}
        doctor = Doctor.objects.get(user=self.request.user)
        context['doctor'] = doctor
        return context

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('doctor_appoint')

    def get(self, request, *args, **kwargs):
        action = kwargs.get('action')
        appoint_pk = kwargs.get('pk')

        if action and appoint_pk:
            appoint = Appointment.objects.get(id=appoint_pk)
            time_tuple = appoint.date_of_appointment.timetuple()
            appoint_time = time.strftime('%d %b, %Y %I:%M %p', time_tuple)
            return_msg_text = f'Appointment @ {appoint_time} with {appoint.student}'

            if action == 'confirm':
                appoint.msg = ''
                appoint.is_confirmed = True
                appoint.is_cancelled = False
                messages.success(request, f'Confirmed: {return_msg_text}')
                appoint.save()

            elif action == 'cancel':
                appoint.is_confirmed = False
                appoint.is_cancelled = True
                appoint.msg = request.GET.get('reason', '')
                messages.error(request, f'Cancelled: {return_msg_text}')
                appoint.save()

        return super().get(self, *args, **kwargs)


class AppointmentCreateView(UserMustBeStudentMixin, CreateView):

    """
    Appoint create view for students.

    It is used to make an appointment with a doctor.
    This views is to be only used by students.
    """

    template_name = 'dashboard/student/dashboard_student_appoint_create.html'
    form_class = AppointmentCreateForm

    def get_success_url(self):
        return reverse_lazy('student_all_appoint')

    def form_valid(self, form):
        data = {
            'doctor': form.cleaned_data.get('doctor'),
            'date_of_appointment': form.cleaned_data.get('date_of_appointment'),
            'student': Student.objects.get(user=self.request.user),
        }

        obj = Appointment.objects.create(**data)
        obj.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(user=self.request.user)
        context['student'] = student
        return context
