"""Views for student app."""

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import TemplateView, View, ListView

from braces.views import AnonymousRequiredMixin

from appointments.models import Appointment
from announcements.models import Announcement
from doctor.models import Doctor
from medicines.models import Medicine
from student.forms import LoginForm
from student.models import Student, VisitHistory
from student.mixins import UserMustBeStudentMixin


class HomePageView(TemplateView):

    """Homepage view."""

    http_method_names = ['get']
    template_name = 'student/home.html'

    def get_context_data(self, **kwargs):
        all_announcements = Announcement.objects.filter(is_posted=True)[:6]
        kwargs.update({'announcements': all_announcements})
        return kwargs


class Login(AnonymousRequiredMixin, LoginView):

    """Login view."""

    authentication_form = LoginForm
    template_name = 'student/login.html'


class LogoutView(View):

    """Logout view."""

    def get(self, request):
        logout(request)
        return redirect('homepage')


class StudentDashboard(UserMustBeStudentMixin, TemplateView):

    """Dashboard view for students."""

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

    """Medicine stock information view for students."""

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

    """Appointments list view for students."""

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

    """List of doctors view."""

    http_method_names = ['get']
    model = Doctor
    queryset = Doctor.objects.filter(is_available=True)
    template_name = 'student/doctors_list.html'


class About(TemplateView):

    """About page view."""

    template_name = 'student/about.html'
