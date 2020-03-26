from django.shortcuts import render, reverse
from django.views.generic import TemplateView, UpdateView, ListView
from django.contrib.auth.mixins import UserPassesTestMixin

from doctor.mixins import UserMustBeDoctorMixin
from doctor.models import Doctor
from doctor.forms import DoctorUpdateProfileForm
from student.models import VisitHistory
from medicines.models import Medicine


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
