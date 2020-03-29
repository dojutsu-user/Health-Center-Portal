"""Admin panel settings medicines app."""

from django.contrib import admin

from medicines.models import Medicine


class MedicineAdmin(admin.ModelAdmin):

    list_display = ['name', 'quantity', 'salt']
    search_fields = [
        'name',
        'salt',
        'additional_details',
    ]
    list_filter = [
        'quantity',
        'is_available',
    ]


admin.site.register(Medicine, MedicineAdmin)
