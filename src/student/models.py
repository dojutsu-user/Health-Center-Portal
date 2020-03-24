"""
Models related to students.
"""
from django.db import models
from django.contrib.auth.models import User

from doctor import models as doctor_models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
