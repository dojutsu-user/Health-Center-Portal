from django.db import models

from student.models import Student
from doctor.models import Doctor


class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    msg = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_of_appointment = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f'From: {self.student}, To: {self.doctor}, Date: {self.date_of_appointment}'
