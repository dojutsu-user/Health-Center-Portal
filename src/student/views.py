from django.views.generic import TemplateView
from braces.views import AnonymousRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import redirect

from student.forms import LoginForm
from doctor.models import Doctor
from student.models import Student
from student.mixins import UserMustBeStudentMixin


class HomePageView(TemplateView):
    http_method_names = ['get']
    template_name = 'student/home.html'


class Login(AnonymousRequiredMixin, LoginView):
    authentication_form = LoginForm
    template_name = 'student/login.html'

    def get_success_url(self):
        form_obj = self.get_form()
        user = form_obj.get_user()
        if Student.objects.filter(user=user).exists():
            pass
        elif Doctor.objects.filter(user=user).exists():
            pass
        return '/'


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('homepage')


class StudentDashboard(UserMustBeStudentMixin, TemplateView):
    http_method_names = ['get']
    template_name = 'dashboard/student/dashboard_student_history.html'

    def get_context_data(self, **kwargs):
        student = Student.objects.get(user=self.request.user)
        kwargs.update({
            'student': student
        })
        return kwargs
