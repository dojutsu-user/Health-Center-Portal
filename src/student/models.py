"""
Models related to students.
"""
import time
from django.db import models
from django.contrib.auth.models import User

from doctor.models import Doctor
from medicines.models import Medicine


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class VisitHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    details = models.TextField('Details', null=True, blank=True)
    timestamp = models.DateTimeField('Date and time of visit')

    class Meta:
        verbose_name_plural = 'Visit histories'

    def __str__(self):
        student_name = self.student.user.get_full_name().title()
        return f'{student_name} - {self.timestamp}'


class MedicineGivenHistory(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    visit = models.ForeignKey(VisitHistory, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Medicine given histories'

    def __str__(self):
        return f'{self.medicine} [{self.quantity}]'
