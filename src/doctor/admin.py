from django.contrib import admin
from doctor.models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Doctor, DoctorAdmin)
