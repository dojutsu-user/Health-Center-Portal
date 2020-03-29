from django.shortcuts import render, reverse
from django.views.generic import TemplateView, UpdateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from doctor.mixins import UserMustBeDoctorMixin
from doctor.models import Doctor
from doctor.forms import DoctorUpdateProfileForm,CustomPasswordChangeForm
from student.models import VisitHistory, Student
from medicines.models import Medicine
from appointments.models import Appointment


class DoctorDashboardView(UserMustBeDoctorMixin, TemplateView):

    http_method_names = ['get']
    template_name = 'dashboard/doctor/dashboard_doctor_profile.html'

    def get_context_data(self, **kwargs):
        doctor = Doctor.objects.get(user=self.request.user)
        kwargs.update({
            'doctor': doctor,
        })
        return kwargs


class DoctorEditProfileView(UserMustBeDoctorMixin, UserPassesTestMixin, UpdateView):
    template_name = 'dashboard/doctor/dashboard_doctor_edit_profile.html'
    form_class = DoctorUpdateProfileForm
    model = Doctor

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(user=self.request.user)
        return qs

    def test_func(self):
        obj = self.get_object()
        return self.request.user.pk == obj.user.pk

    def get_success_url(self):
        obj = self.get_object()
        return reverse('doctor_edit_profile', kwargs={'pk': obj.pk})


class DoctorListOfPatientsView(UserMustBeDoctorMixin, ListView):
    http_method_names = ['get']
    model = VisitHistory
    ordering = 'timestamp'
    template_name = 'dashboard/doctor/dashboard_doctor_patients_list.html'

    def get_queryset(self):
        doctor_obj = Doctor.objects.get(user=self.request.user)
        return VisitHistory.objects.filter(doctor=doctor_obj)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor = Doctor.objects.get(user=self.request.user)
        context['doctor'] = doctor
        return context


class DoctorMedicineStockView(UserMustBeDoctorMixin, ListView):
    http_method_names = ['get']
    model = Medicine
    ordering = 'name'
    template_name = 'dashboard/doctor/dashboard_doctor_medicine_stock.html'
    queryset = Medicine.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor = Doctor.objects.get(user=self.request.user)
        context['doctor'] = doctor
        return context


class DoctorSearchView(UserMustBeDoctorMixin, ListView):
    http_method_names = ['get']
    model = Medicine
    template_name = 'dashboard/doctor/dashboard_doctor_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor = Doctor.objects.get(user=self.request.user)
        context['doctor'] = doctor
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return Student.objects.none()
        return Student.objects.filter(
            Q(user__email__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        )


class DoctorStudentDetail(UserMustBeDoctorMixin, ListView):
    http_method_names = ['get']
    model = VisitHistory
    template_name = 'dashboard/doctor/dashboard_doctor_student_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor = Doctor.objects.get(user=self.request.user)
        context['doctor'] = doctor

        student_pk = self.kwargs.get('pk')
        student  = Student.objects.get(id=student_pk)
        student_name = student.user.get_full_name().title()
        student_email = student.user.email.lower()
        context['student_name'] = student_name
        context['student_email'] = student_email
        return context

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        if pk is None:
            return VisitHistory.objects.none()
        return VisitHistory.objects.filter(student__pk=pk).order_by('-timestamp')


class DoctorPasswordChangeView(UserMustBeDoctorMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    http_method_names = ['get', 'post']
    template_name = 'dashboard/doctor/dashboard_doctor_password_change.html'
    success_message = 'Password Changed Successfully.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor = Doctor.objects.get(user=self.request.user)
        context['doctor'] = doctor
        return context

    def get_success_url(self):
        return reverse_lazy('doctor_password_change')


class DoctorAppointmentView(UserMustBeDoctorMixin, ListView):
    
    model = Appointment
    template_name = 'dashboard/doctor/dashboard_doctor_appointments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctor = Doctor.objects.get(user=self.request.user)
        context['doctor'] = doctor
        return context
    
    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(doctor__user=user).order_by('-date_created')
