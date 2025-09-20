from __future__ import absolute_import, unicode_literals

from .celery import app as celery_app
# This ensures all background tasks use the same Celery manager,
# and you don’t have to create a new one in every app.
__all__ = ('celery_app',)