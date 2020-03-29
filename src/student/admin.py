"""Admin panel settings for student app."""

from django.contrib import admin

from student.models import Student, VisitHistory, MedicineGivenHistory


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
