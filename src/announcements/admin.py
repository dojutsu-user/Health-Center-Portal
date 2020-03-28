from django.contrib import admin

from announcements.models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):

    list_filter = [
        'date_posted',
        'is_posted',
        'author',
    ]
    list_display = [
        'title',
        'date_posted',
        'is_posted',
    ]

    def get_readonly_fields(self, request, obj=None):
        
        if not request.user.is_superuser:
            return [
                'author',
                'slug',
            ]
        return []

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Announcement, AnnouncementAdmin)
