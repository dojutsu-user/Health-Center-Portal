"""
health_center_portal URL Configuration.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from student.views import HomePageView, Login, LogoutView, ListOfDoctors, About


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('available-doctors/', ListOfDoctors.as_view(), name='available_doctors'),
    path('about/', About.as_view(), name='about'),
    path('accounts/', include('allauth.urls')),

    path('student/', include('student.urls')),
    path('doctor/', include('doctor.urls')),
    path('announcement/', include('announcements.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
