from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nzfnx!ppz-6swhuk*0k86ghx4oxcb6v%^6#6-_so7uz7ck(g69'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["adminsicreo.gficr.com", "localhost", "127.0.0.1", '172.16.8.183']
APPEND_SLASH = False

X_FRAME_OPTIONS = 'DENY'

#CSP_DEFAULT_SRC = ("'self'",)

# Application definition

INSTALLED_APPS = [
    'apps.contact',
    'apps.form',
    'apps.question',
    'apps.response',
    'apps.salesPoint',
    'apps.survey',
    'apps.users',
    'apps.zone',
    'apps.division',
#    'corsheaders',
#=================^APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'farmanova_csat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'farmanova_csat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": os.environ.get("SQL_NAME", "sicreo"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "172.16.8.227"),
        "PORT": "",
        'OPTIONS': {
            # String. ODBC Driver to use ("ODBC Driver 17 for SQL Server", 
            # "SQL Server Native Client 11.0", "FreeTDS" etc). 
            # Default is "ODBC Driver 17 for SQL Server".
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Costa_Rica'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Permitir CORS

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "http://sicreo.gficr.com",
    'http://172.16.8.183:8000'
  
    
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

#CSRF_COOKIE_SECURE = True
#CSRF_COOKIE_HTTPONLY = True
#SESSION_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = ['http://adminsicreo.gficr.com']
#SECURE_CROSS_ORIGIN_OPENER_POLICY = None