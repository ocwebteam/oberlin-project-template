import os
here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Oberlin College Webteam', 'webteam@oberlin.edu'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': here('..','{{ project_name }}.db'),
	}
}

SECRET_KEY = '{{ secret_key }}'
ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Templates

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

# Middleware

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

# Static and Media files

MEDIA_ROOT = here('..', 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = here('..', 'static')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'compressor.finders.CompressorFinder',
)

# Compressor

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = (
	'compressor.filters.css_default.CssAbsoluteFilter',
	'compressor.filters.cssmin.CSSMinFilter',
)

# Apps

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'grappelli',
	'django.contrib.admin',
	'south',
	'compressor',
	'typogrify',
)