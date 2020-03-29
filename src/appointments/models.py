"""Models related to appointments app."""

from django.db import models

from doctor.models import Doctor
from student.models import Student


class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        limit_choices_to={'is_available': True}
    )
    msg = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_of_appointment = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        from_ = f'From: {self.student}'
        to = f'To: {self.doctor}'
        date = f'Date: {self.date_of_appointment}'
        return f'{from_}, {to} @ {date}'
