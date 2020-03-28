from django.urls import path

from announcements.views import AnnouncementDetailView


urlpatterns = [
    path('<str:slug>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
]
