from django.contrib import admin

from medicines.models import Medicine


class MedicineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Medicine, MedicineAdmin)
