"""
Models related to doctor.
"""
import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings

from doctor import utils


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Display Picture', upload_to=utils.image_upload_util, validators=[utils.image_file_size_validator])
    name = models.CharField('Name', max_length=50)
    about = models.TextField('About The Doctor')
    education = models.TextField('Education Details')
    available_description = models.TextField('Availability')

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return f'{self.name.title()}'
