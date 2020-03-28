from django.urls import path

from appointments.views import AppointmentUpdateView


urlpatterns = [
    path('update/<int:pk>/<str:action>/', AppointmentUpdateView.as_view(), name='appoint_update'),
]