# -*- encoding: UTF-8 -*-

import os

# Paths -- Build paths like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_TEST_ROOT = os.path.join(BASE_DIR, 'media_tests')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')

# URLs
STATIC_URL = '/investigacion/static/'
MEDIA_URL = '/investigacion/media/'
MEDIA_TEST_URL = '/media_tests/'
LOGIN_URL = 'login'  # Login address for login_required decorator
BASE_URL = 'http://wwwpre.ull.es/portaldeinvestigacion'
OLD_PORTAL_URL = 'http://aportalpre.stic.ull.es'
TINYMCE_JS_URL = os.path.join(STATIC_URL, 'tiny_mce/tiny_mce.js')
TINYMCE_JS_TEXTAREA = os.path.join(STATIC_URL, 'tiny_mce/conf/textarea.js')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z7(##tnkvh@@h@rcpcu+&v=nyy!(nt1y6a8ovb5l7yk04bxh3+'

# Enable translation of strings in this file
_ = lambda s: s


ADMINS = (
    ('STIC-Investigacion', 'stic.investigacion@ull.es'),
)
MANAGERS = ADMINS

# Internationalization
LANGUAGES = (
    ('es', 'Español'),
    ('en', 'English'),
)
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'es'
TIME_ZONE = 'Atlantic/Canary'
USE_TZ = True
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'core/locale'),
    os.path.join(BASE_DIR, 'cvn/locale'),
    os.path.join(BASE_DIR, 'statistics/locale'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.sites',
    'tinymce',
    'south',
    'core',
    'cvn',
    'crequest',
    'statistics',
    'django_coverage',
    'django_tables2',
    'mptt',
    'modeltranslation',
    'flatpages_i18n',
)

COVERAGE_MODULE_EXCLUDES = (
    'tests$', 'settings$', 'urls$', 'locale$', 'common.views.test', '__init__',
    'django', 'migrations', 'south$', 'debug_toolbar$', 'crequest$', 'admin$',
    'management$')

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'crequest.middleware.CrequestMiddleware',
    'flatpages_i18n.middleware.FlatpageFallbackMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'core.backends.CASBackend',
)

# Development and debugging configuration
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEVEL = True

# Set ID for flatpages
SITE_ID = 1  # REQUIRED FOR 'django.contrib.flatpages'

# Authentication CAS - ULL
CAS_SERVER_URL = 'https://loginpruebas.ull.es/cas-1/'
CAS_ADMIN_PREFIX = 'admin'  # The URL prefix of the Django administration site.
CAS_EXTRA_LOGIN_PARAMS = ''  # Extra parameters for login URL when redirecting
# If `True`, logging out of the application will always send the user
# to the URL specified by `CAS_REDIRECT_URL`.
CAS_IGNORE_REFERER = False
# If `False`, logging out of the application won't log the user out
# of CAS as well.
CAS_LOGOUT_COMPLETELY = True
CAS_REDIRECT_URL = '/investigacion/'  # Redirect here when no referrer
# If `True` and an unknown or invalid ticket is received,
# the user is redirected back to the login page.
CAS_RETRY_LOGIN = True
#  The CAS protocol version to use.
# `'1'` and `'2'` are supported, with `'2'` being the default.
CAS_VERSION = 'CAS_2_SAML_1_0'
CAS_GRUPOS_NOAUT = ['INSTITUCIONAL']


ROOT_URLCONF = 'investigacion.urls'

WSGI_APPLICATION = 'investigacion.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'memviinv',
        'USER': 'viinv',
        'PASSWORD': '1234',
        'HOST': '',
        'PORT': '',
    },
}


SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

LOG_FILENAME = os.path.join(PROJECT_ROOT, 'cvn.log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s \
                       <%(pathname)> --- %(message)s',
            'datefmt': '%d-%m-%Y %H:%M:%S'
        },
        'standard': {
            'format': '[%(levelname)s] %(asctime)s --- %(message)s',
            'datefmt': '%d-%m-%Y %H:%M:%S'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        # NullHandler, which will pass any DEBUG (or higher)
        # message to /dev/null.
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        # StreamHandler, which will print any DEBUG (or higher)
        #  message to stderr.
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILENAME,
            'maxBytes': 4096 * 1024 * 1024,        # 4MB para rotar de fichero
            'backupCount': 5,
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILENAME,
            'maxBytes': 4096 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'standard'
        },
        'mail_admins': {
            'level': 'ERROR',             # Errores de la serie 5XX
            'filters': ['require_debug_false'],  # Only if DEBUG=False
            'class': 'django.utils.log.AdminEmailHandler',
            # Incluye la petición y la traza del error en el mail.
            'include_html': True
        },
        'find_pairs_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'find_pairs.log'
        },
    },
    'loggers': {
        'cvn': {
            'handlers': ['default', 'mail_admins'],
            'level': 'INFO',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'ERROR',
            'propagate': False
        },
        'cvn.management.commands.find_pairs': {
            'level': 'DEBUG',
            'handlers': ['find_pairs_handler'],
            'propagate': False
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "core.context_processors.extra_info",
    "cvn.context_processors.extra_info",
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'cvn/templates'),
    os.path.join(BASE_DIR, 'core/templates'),
    os.path.join(BASE_DIR, 'statistics/templates'),
)


STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# ****************************** WEB SERVICES ******************************

WS_SERVER_URL = 'http://django1-pre.stic.ull.es/odin/core/rest/'

# ALL CATEGORIES
WS_CATEGORIES = WS_SERVER_URL + 'get_cce?past_days=%s'

# RRHH_CODE OF AN USER
WS_COD_PERSONA = WS_SERVER_URL + 'get_codpersona?nif=%s'

# TODO: INFO OF AN USER
WS_INFO_PDI = WS_SERVER_URL + 'get_info_pdi?cod_persona=%s'

# TODO: INFO OF AN USER BY YEARS
WS_INFO_PDI_YEAR = WS_SERVER_URL + 'get_info_pdi?cod_persona=%s&ano=%s'

# ALL CURRENT DEPARTMENTS
WS_DEPARTMENTS = WS_SERVER_URL + 'get_departamentos_y_miembros'

# ALL DEPARTMENTS BY YEARS
WS_DEPARTMENTS_YEAR = WS_SERVER_URL + 'get_departamentos_y_miembros?year=%s'

# TODO: INFO OF A DEPARTMENT
WS_INFO_DEPARTMENT = (WS_SERVER_URL +
                      'get_info_departamento?cod_departamento=%s')

# TODO: CODES OF ALL CURRENT DEPARTMENTS
WS_CODES_DEPARTMENTS = WS_SERVER_URL + 'get_departamentos'

# TODO: CODES OF ALL DEPARTMENTS BY YEARS
WS_CODES_DEPARTMENTS_YEAR = WS_SERVER_URL + 'get_departamentos?year=%s'

# CURRENT DEPARTMENT AND ITS MEMBERS OF AN USER
WS_DEPARTMENT_USER = (
    WS_SERVER_URL +
    'get_departamentos_y_miembros?cod_persona=%s')

# TODO: DEPARTMENT AND ITS MEMBERS OF AN USER BY YEARS
WS_DEPARTMENT_USER_YEAR = (
    WS_SERVER_URL +
    'get_departamentos_y_miembros?cod_persona=%s&year=%s')

# CURRENT DETAILS OF A DEPARTMENT
WS_DEPARTMENT = (
    WS_SERVER_URL +
    'get_departamentos_y_miembros?codigo=%s')

# DETAILS OF A DEPARTMENT BY YEARS
WS_DEPARTMENT_YEAR = (
    WS_SERVER_URL +
    'get_departamentos_y_miembros?codigo=%s&year=%s')

# TODO: USERS BY UNIDAD AND YEAR
WS_PDI_VALID_UNIDAD_YEAR = (WS_SERVER_URL +
                            'get_pdi_vigente?cod_%s=%s&year=%s')

# ALL CURRENT AREAS
WS_ALL_AREAS = WS_SERVER_URL + 'get_areas_y_miembros'

# INFO OF AN AREA
WS_INFO_AREA = WS_SERVER_URL + 'get_info_area?cod_area=%s'

# CODES OF ALL CURRENT AREAS
WS_CODES_AREAS = WS_SERVER_URL + 'get_areas'

# CODES OF ALL AREAS BY YEARS
WS_CODES_AREAS_YEAR = WS_SERVER_URL + 'get_areas?year=%s'

# AREA AND ITS MEMBERS OF AN USER
WS_AREA_USER = (
    WS_SERVER_URL +
    'get_area_y_miembros?cod_persona=%s')

# AREA AND ITS MEMBERS OF AN USER BY YEARS
WS_AREA_USER_YEAR = (
    WS_SERVER_URL +
    'get_area_y_miembros?cod_persona=%s&year=%s')

# DETAILS OF A AREA
WS_AREA = (
    WS_SERVER_URL +
    'get_area_y_miembros?cod_area=%s')

# DETAILS OF A DEPARTMENT BY YEARS
WS_AREA_YEAR = (
    WS_SERVER_URL +
    'get_area_y_miembros?cod_area=%s&year=%s')

# ****************************** END WEB SERVICES ******************************

# REDIS
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None
# Seconds
REDIS_TIMEOUT = 86400  # One Day

try:
    SETTINGS_LOCAL
except NameError:
    try:
        from settings_local import *
    except ImportError:
        pass
