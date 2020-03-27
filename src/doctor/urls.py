from django.urls import path

from doctor.views import DoctorDashboardView, DoctorEditProfileView, DoctorListOfPatientsView, DoctorMedicineStockView, DoctorSearchView, DoctorStudentDetail, DoctorPasswordChangeView

urlpatterns = [
    path('dashboard/', DoctorDashboardView.as_view(), name='doctor_dashboard'),
    path('dashboard/edit-profile/<int:pk>', DoctorEditProfileView.as_view(), name='doctor_edit_profile'),
    path('dashboard/list-of-patients/', DoctorListOfPatientsView.as_view(), name='doctor_patient_list'),
    path('dashboard/medicines-stock/', DoctorMedicineStockView.as_view(), name='doctor_medicine_info'),
    path('dashboard/search/', DoctorSearchView.as_view(), name='doctor_search'),
    path('dashboard/student-details/<int:pk>', DoctorStudentDetail.as_view(), name='doctor_student_detail'),
    path('dashboard/password-change', DoctorPasswordChangeView.as_view(), name='doctor_password_change'),
]
