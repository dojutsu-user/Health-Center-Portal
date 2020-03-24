from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from student.models import Student


class UserMustBeStudentMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not Student.objects.filter(user=user).exists():
            raise PermissionDenied('You are not authorized to access this page.')
        return super().dispatch(request, *args, **kwargs)
