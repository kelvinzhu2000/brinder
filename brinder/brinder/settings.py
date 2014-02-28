# Django settings for brinder project.

import yaml
import os

def get_conf(yaml_path):
    yfile = file(yaml_path, 'r')

    yconf = yaml.load(yfile)
    conf = {}

    if 'common' in yconf:
        common = yconf['common']

        # everything else should map 1-to-1
        conf.update(common)

    return conf

PROJECT_PATH = os.path.join(os.path.dirname(__file__), '')
CONF_PATH = 'conf.yaml'

ENV_CONF_PATH = os.path.join(PROJECT_PATH, CONF_PATH)

env_conf            = get_conf(ENV_CONF_PATH)
env_db_conf         = env_conf['db']
env_debug_conf      = env_conf['debug']
env_media_conf      = env_conf['media']
env_secret_key_conf = env_conf['secret_key']
env_runserver_conf  = env_conf['use_runserver']
env_south_conf      = env_conf['use_south']

DEBUG = env_debug_conf
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': env_db_conf['engine'], # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': env_db_conf['name'],     # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': env_db_conf['user'],
        'PASSWORD': env_db_conf['password'],
        'HOST': env_db_conf['host'],     # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': env_db_conf['port'],     # Set to empty string for default.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = env_media_conf['root']

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = env_media_conf['url']


LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    env_media_conf['dir'],
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = env_secret_key_conf

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'brinder.urls'

if env_runserver_conf:
    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = 'brinder.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

if env_south_conf:
    south = 'south'
else:
    # using this module as a dummy one in case we can't use south
    south = 'django.contrib.admindocs'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'surveys',
    'emails',
    'registration',
    south,
)


