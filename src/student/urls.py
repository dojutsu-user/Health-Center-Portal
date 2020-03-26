from django.urls import path

from student.views import StudentDashboard, MedicineStockView

urlpatterns = [
    path('dashboard/', StudentDashboard.as_view(), name='student_dashboard'),
    path('dashboard/medicines-stock/', MedicineStockView.as_view(), name='student_medicines_stock'),
]
