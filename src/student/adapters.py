from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from allauth.exceptions import ImmediateHttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from student.models import Student


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        email = sociallogin.user.email
        for allowed_domain in settings.ALLOWED_EMAIL_DOMAINS_FOR_SIGNUP:
            if not allowed_domain in email:
                messages.error(request, 'Unable to login with the email provided.')
                raise ImmediateHttpResponse(HttpResponseRedirect(reverse('login')))

    def save_user(self, *args, **kwargs):
        user = super().save_user(*args, **kwargs)
        student = Student.objects.create(user=user)
        student.save()
        return user
