"""Utility mixins related to student app."""

from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

from student.models import Student


class UserMustBeStudentMixin(AccessMixin):

    """Checks if the user is authenticated and is a student or not."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not Student.objects.filter(user=request.user).exists():
            raise PermissionDenied(
                'You are not authorized to access this page.'
            )

        return super().dispatch(request, *args, **kwargs)
