"""urls.py for doctor app."""

from django.urls import path

from doctor import views as doctor_views

urlpatterns = [
    path(
        'dashboard/',
        doctor_views.DoctorDashboardView.as_view(),
        name='doctor_dashboard',
    ),
    path(
        'dashboard/edit-profile/<int:pk>/',
        doctor_views.DoctorEditProfileView.as_view(),
        name='doctor_edit_profile'
    ),
    path(
        'dashboard/list-of-patients/',
        doctor_views.DoctorListOfPatientsView.as_view(),
        name='doctor_patient_list'
    ),
    path(
        'dashboard/medicines-stock/',
        doctor_views.DoctorMedicineStockView.as_view(),
        name='doctor_medicine_info'
    ),
    path(
        'dashboard/search/',
        doctor_views.DoctorSearchView.as_view(),
        name='doctor_search'
    ),
    path(
        'dashboard/student-details/<int:pk>/',
        doctor_views.DoctorStudentDetail.as_view(),
        name='doctor_student_detail'
    ),
    path(
        'dashboard/password-change/',
        doctor_views.DoctorPasswordChangeView.as_view(),
        name='doctor_password_change'
    ),
    path(
        'dashboard/appointments/',
        doctor_views.DoctorAppointmentView.as_view(),
        name='doctor_appoint'
    ),
]
