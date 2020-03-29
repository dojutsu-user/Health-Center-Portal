from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from braces.views import AnonymousRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import View, ListView
from django.contrib.auth import logout
from django.shortcuts import redirect

from student.forms import LoginForm
from doctor.models import Doctor
from medicines.models import Medicine
from student.models import Student, VisitHistory
from student.mixins import UserMustBeStudentMixin
from announcements.models import Announcement
from appointments.models import Appointment


class HomePageView(TemplateView):
    http_method_names = ['get']
    template_name = 'student/home.html'

    def get_context_data(self, **kwargs):
        all_announcements = Announcement.objects.filter(is_posted=True)[:6]
        kwargs.update({ 'announcements': all_announcements })
        return kwargs


class Login(AnonymousRequiredMixin, LoginView):
    authentication_form = LoginForm
    template_name = 'student/login.html'


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('homepage')


class StudentDashboard(UserMustBeStudentMixin, TemplateView):
    http_method_names = ['get']
    template_name = 'dashboard/student/dashboard_student_history.html'

    def get_context_data(self, **kwargs):
        student = Student.objects.get(user=self.request.user)
        visits = VisitHistory.objects.filter(student=student)

        kwargs.update({
            'student': student,
            'visits': visits,
        })
        return kwargs


class MedicineStockView(UserMustBeStudentMixin, TemplateView):
    http_method_names = ['get']
    template_name = 'dashboard/student/dashboard_student_medicine_stock.html'

    def get_context_data(self, **kwargs):
        student = Student.objects.get(user=self.request.user)
        medicines = Medicine.objects.all()

        kwargs.update({
            'student': student,
            'medicines': medicines,
        })
        return kwargs


class StudentAppointmentListView(UserMustBeStudentMixin, ListView):

    template_name = 'dashboard/student/dashboard_student_appoint_list.html'
    model = Appointment

    def get_queryset(self):
        return Appointment.objects.filter(student__user=self.request.user).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(user=self.request.user)
        context['student'] = student
        return context


class ListOfDoctors(ListView):
    http_method_names = ['get']
    model = Doctor
    queryset = Doctor.objects.filter(is_available=True)
    template_name = 'student/doctors_list.html'


class About(TemplateView):
    template_name = 'student/about.html'
