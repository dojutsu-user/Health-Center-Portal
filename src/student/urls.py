from django.urls import path

from student.views import StudentDashboard, MedicineStockView, StudentAppointmentListView
from appointments.views import AppointmentCreateView

urlpatterns = [
    path('dashboard/', StudentDashboard.as_view(), name='student_dashboard'),
    path('dashboard/medicines-stock/', MedicineStockView.as_view(), name='student_medicines_stock'),
    path('dashboard/new-appointment/', AppointmentCreateView.as_view(), name='student_appoint_create'),
    path('dashboard/all-appointments/', StudentAppointmentListView.as_view(), name='student_all_appoint'),
]
