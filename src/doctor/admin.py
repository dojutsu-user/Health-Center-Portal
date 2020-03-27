from django.contrib import admin
from doctor.models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Doctor, DoctorAdmin)
