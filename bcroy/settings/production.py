from django.conf import settings
DEBUG= False
DATABASES=settings.DATABASES

ALLOWED_HOSTS = ['*']

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)