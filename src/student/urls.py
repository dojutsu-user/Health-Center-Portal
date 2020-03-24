from django.urls import path

from student.views import HomePageView, Login, LogoutView, StudentDashboard

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('student/dashboard', StudentDashboard.as_view(), name='student_dashboard'),
]