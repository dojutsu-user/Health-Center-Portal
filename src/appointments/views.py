import time
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View, RedirectView
from django.urls import reverse_lazy
from django.contrib import messages

from doctor.mixins import UserMustBeDoctorMixin
from appointments.models import Appointment
from doctor.models import Doctor
from student.mixins import UserMustBeStudentMixin


class AppointmentUpdateView(UserMustBeDoctorMixin, RedirectView):

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
