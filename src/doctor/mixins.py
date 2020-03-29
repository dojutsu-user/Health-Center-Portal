"""Useful mixins related to doctor app."""

from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

from doctor.models import Doctor


class UserMustBeDoctorMixin(AccessMixin):

    """
    This checks if the user is a doctor or not.
    
    It raises `PermissionDenied` error if the user is not a doctor. 
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not Doctor.objects.filter(user=request.user).exists():
            raise PermissionDenied('You are not authorized to access this page.')

        return super().dispatch(request, *args, **kwargs)
