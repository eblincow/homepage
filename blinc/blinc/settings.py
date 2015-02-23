"""
homepage blinc
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


DIR_1 = os.path.dirname(os.path.dirname(__file__))
DIR_0 = '/'.join(DIR_1.split('/')[:-1]) + "/"
DIR_2 = os.path.join(DIR_1, 'blinc')


# Change when in production
SECRET_KEY = '6qbb6a70ss+r!z9ictzp^evy-+w+6c5!0d%n6d$#wq&=y5fku_'


IS_PRODUCTION = False   #this will be replaced by the package builder with a True/False.

DEBUG = not IS_PRODUCTION

TEMPLATE_DEBUG = True

if IS_PRODUCTION:
    ALLOWED_HOSTS = ['localhost', '.amazonaws.com']
else:
    ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blinc.urls'

WSGI_APPLICATION = 'blinc.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DIR_1, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'


TEMPLATE_DIRS = (
    os.path.join(DIR_2, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(DIR_2, "static"),
)


USERNAMES = ['eb']