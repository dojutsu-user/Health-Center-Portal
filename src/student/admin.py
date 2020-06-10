"""Admin panel settings for student app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from student.models import Student, VisitHistory, MedicineGivenHistory


admin.site.unregister(User)


class StudentAdmin(admin.ModelAdmin):
    pass


class MedicineGivenHistoryInline(admin.TabularInline):

    model = MedicineGivenHistory


class VisitHistoryAdmin(admin.ModelAdmin):

    list_display = [
        'student',
        'doctor',
        'timestamp',
    ]
    search_fields = [
        'student',
        'doctor'
    ]
    list_filter = [
        'timestamp',
        'student',
        'doctor',
    ]
    inlines = [
        MedicineGivenHistoryInline
    ]

    def has_change_permission(self, request, obj=None):

        if not request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):

        if not request.user.is_superuser:
            return False
        return True


class CustomUserAdmin(UserAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(username=request.user.username)
        return qs

    def get_form(self, request, obj=None, **kwargs):

        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if (
            not is_superuser
            and obj is not None
            and obj == request.user
        ):
            disabled_fields |= {
                'username',
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
                'last_login',
                'date_joined',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form


admin.site.register(Student, StudentAdmin)
admin.site.register(VisitHistory, VisitHistoryAdmin)
admin.site.register(User, CustomUserAdmin)
