"""
homepage blinc
"""

import os

# Directory structure
DIR_1 = os.path.dirname(os.path.dirname(__file__))
DIR_0 = '/'.join(DIR_1.split('/')[:-1]) + "/"
DIR_2 = os.path.join(DIR_1, 'blinc')


SECRET_KEY = '6qbb6a70ss+r!z9ictzp^evy-+w+6c5!0d%n6d$#wq&=y5fku_'

IS_PRODUCTION = False   #this will be replaced by the package builder with a True/False.
DEBUG = not IS_PRODUCTION
TEMPLATE_DEBUG = DEBUG

if IS_PRODUCTION:
    ALLOWED_HOSTS = ['.eblincow.com', '.appspot.com']
else:
    ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'sslserver',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
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




