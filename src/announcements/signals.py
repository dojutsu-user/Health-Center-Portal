"""Signals related to announcements app."""

from django.db.models.signals import post_save

from announcements.models import Announcement
from announcements.utils import unique_slug_generator


def generate_slug(sender, instance, created, *args, **kwargs):
    """Updates the slug of the Announcement model instance."""

    if created:
        slug = unique_slug_generator(instance)
        instance.slug = slug
        instance.save()


post_save.connect(generate_slug, sender=Announcement)
