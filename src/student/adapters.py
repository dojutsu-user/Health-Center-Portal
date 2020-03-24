from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.forms import ValidationError

from student.models import Student


class CustomAccountAdapter(DefaultAccountAdapter):

    def clean_email(self, email):
        email = super().__init__(email)
        for allowed_domain in ['@iiitl.ac.in']:
            if allowed_domain not in email.lower():
                raise ValidationError('Please login with email provided by your organisation.')
        return email


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, *args, **kwargs):
        user = super().save_user(*args, **kwargs)
        student = Student.objects.create(user=user)
        student.save()
        return user
