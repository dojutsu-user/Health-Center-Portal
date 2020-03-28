from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from student.models import Student, VisitHistory, MedicineGivenHistory

admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    
    def get_readonly_fields(self, request, obj=None):

        readonly_fields = [
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
            'last_login',
            'date_joined',
        ]

        if not request.user == obj:
            readonly_fields += [
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
            ]

        return readonly_fields


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



admin.site.register(Student, StudentAdmin)
admin.site.register(VisitHistory, VisitHistoryAdmin)
