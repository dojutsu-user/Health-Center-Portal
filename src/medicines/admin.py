from django.contrib import admin

from medicines.models import Medicine


class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'salt']


admin.site.register(Medicine, MedicineAdmin)
