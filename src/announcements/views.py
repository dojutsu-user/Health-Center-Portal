"""Views for announcements app."""

from django.views.generic import DetailView

from announcements.models import Announcement


class AnnouncementDetailView(DetailView):

    http_method_names = ["get"]
    template_name = "announcements/announcement_detail.html"
    model = Announcement
    queryset = Announcement.objects.filter(is_posted=True)
