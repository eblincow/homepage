"""
homepage blinc
"""

import os

# Directory structure
DIR_1 = os.path.dirname(os.path.dirname(__file__))
DIR_0 = '/'.join(DIR_1.split('/')[:-1]) + "/"
DIR_2 = os.path.join(DIR_1, 'blinc')

SECRET_KEY = '6qbb6a70ss+r!z9ictzp^evy-+w+6c5!0d%n6d$#wq&=y5fku_'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['.eblincow.com', '.appspot.com']


GZIP_CONTENT_TYPES = (
    'text/css',
    'application/javascript',
    'application/x-javascript',
    'text/javascript'
)


INSTALLED_APPS = (
    'google.appengine',
    'django.contrib.staticfiles',
    'blinc',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blinc.urls'
WSGI_APPLICATION = 'blinc.wsgi.application'
DATABASES = {}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SESSION_EXPIRE_AT_BROWSER_CLOSE=True



STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(DIR_2, 'templates'),
    os.path.join(DIR_2, 'client_apps/templates'),
)

STATICFILES_DIRS = (
    os.path.join(DIR_2, "static"),
)

USERNAMES = {'eb':'arcolight'}
EMAIL = "eric@eblincow.com"




