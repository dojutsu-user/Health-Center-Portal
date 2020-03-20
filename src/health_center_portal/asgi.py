"""
ASGI config for health_center_portal project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_center_portal.settings')

application = get_asgi_application()
