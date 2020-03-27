from django import template
from django.contrib.auth.models import User

from student.models import Student
from doctor.models import Doctor

register = template.Library()


@register.simple_tag
def get_user_type(pk):
    pk = int(pk)
    if Student.objects.filter(user__pk=pk).exists():
        return "student"
    elif Doctor.objects.filter(user__pk=pk).exists():
        return "doctor"
    elif User.objects.filter(pk=pk, is_staff=True).exists():
        return "staff"
