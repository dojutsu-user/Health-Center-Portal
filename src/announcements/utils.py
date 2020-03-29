"""Utility functions for announcements model."""

import string
import random

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """
    Generates and returns a random string of given size.

    :size: Size of the desired random string. Default is 10
    :type size: int
    :param chars: Characters from which random string is to be generated.
        Default value is `abcdefghijklmnopqrstuvwxyz0123456789`
    :type chars: str
    :returns: A random string.
    :rtype: str
    """

    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    Generates and returns a unique slug for the instance.
    It assumes that the `instance` have a `title` and `slug` field.
    The maximum length of the returned slug is 50.

    :instance: Instance for which the unique slug is needed
    :type instance: announcements.models.Announcement
    :new_slug: Slug for the instance.
    :type new_slug: str
    :returns: A unique slug based on the `instance.title`
    :rtpe: str
    """

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)[:46]

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug[:50]).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug[:46],
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug[:50]
