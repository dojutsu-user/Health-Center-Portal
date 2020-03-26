from django.contrib import admin

from student.models import Student, VisitHistory, MedicineGivenHistory


class StudentAdmin(admin.ModelAdmin):
    pass


class MedicineGivenHistoryInline(admin.TabularInline):
    
    model = MedicineGivenHistory


class VisitHistoryAdmin(admin.ModelAdmin):
    
    inlines = [
        MedicineGivenHistoryInline
    ]


admin.site.register(Student, StudentAdmin)
admin.site.register(VisitHistory, VisitHistoryAdmin)
