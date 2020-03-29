"""Models related to announcement app."""

from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Announcement(models.Model):
    title = models.CharField('Title', max_length=100)
    body = RichTextField('Body', config_name='announcements-toolbar')
    date_posted = models.DateField(null=True, blank=True)
    is_posted = models.BooleanField(default=False)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        limit_choices_to={'is_staff': True},
        null=True,
    )
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title
