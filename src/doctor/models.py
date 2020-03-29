"""Models related to doctor app."""

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from doctor import utils


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        'Display Picture',
        upload_to=utils.image_upload_util,
        validators=[
            utils.image_file_size_validator,
        ],
        default='doctor_default.png',
    )
    name = models.CharField('Name', max_length=50)
    about = models.TextField('About The Doctor')
    education = models.TextField('Education Details')
    available_description = models.TextField('Availability')
    is_available = models.BooleanField(
        'Is The Doctor Available?',
        default=True,
    )

    def __str__(self):
        return f'{self.get_name()} - {self.user.email}'

    def get_name(self):
        return f'{self.name.title()}'
