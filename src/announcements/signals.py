from django.db.models.signals import post_save

from announcements.utils import unique_slug_generator
from announcements.models import Announcement


def generate_slug(sender, instance, created, *args, **kwargs):

    if created:
        slug = unique_slug_generator(instance)
        instance.slug = slug
        instance.save()


post_save.connect(generate_slug, sender=Announcement)
