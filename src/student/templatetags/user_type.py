"""Template tags related to student app."""

from django import template
from django.contrib.auth.models import User

from student.models import Student
from doctor.models import Doctor


register = template.Library()


@register.simple_tag
def get_user_type(pk):
    """
    Checks the type of the authenticated user.

    It returns 'student' if the user is student,
    'doctor' if the user is a doctor and
    'staff' if the user is staff member.
    :pk: Primary key of the authenticated user.
    :returns: Type of the user
    :rtype: str
    """

    pk = int(pk)

    if Student.objects.filter(user__pk=pk).exists():
        return "student"
    elif Doctor.objects.filter(user__pk=pk).exists():
        return "doctor"
    elif User.objects.filter(pk=pk, is_staff=True).exists():
        return "staff"
