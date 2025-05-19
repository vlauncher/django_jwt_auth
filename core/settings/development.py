from core.settings.base import *

DEBUG = environ.get('DEBUG')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'