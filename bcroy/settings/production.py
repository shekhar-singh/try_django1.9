#!/usr/bin/python
# -*- coding: <encoding name> -*-
import os
from django.conf import settings

DEBUG= False
DATABASES=settings.DATABASES

ALLOWED_HOSTS = ['*']

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# STATIC_URL = '/static/'

# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = [
#     os.path.join(PROJECT_ROOT, 'static'),
# ]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'