"""
Django settings for Ali project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
# settings.py
import os
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"  # Ajusta la ruta según la estructura de tu proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROTECTED_VIEW_PASSWORD = 'Bared664'

CRONJOBS = [
    ('* * * * *', 'cuentas.tasks.actualizar_estado_vencimiento'),  # Ejecutar cada minuto
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6w-bf$j&#vusp07)l4okv%6p*erx!v(9#c*30$zbl*(@9k+3r#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['192.168.1.79','*']




# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Aplicaciones.Trabajo',
    'Aplicaciones.cuentas',
    'Aplicaciones.Calidad',
    'Aplicaciones.Recepcion',
    'Aplicaciones.Produccion',
    'django.contrib.humanize',
    'corsheaders'

] 
CORS_ALLOWED_ORIGINS = [
    'https://alifrutworkpress-bbhbdhdqebdqf9a3.eastus-01.azurewebsites.net',
]

CSRF_TRUSTED_ORIGINS = [
    'https://alifrutworkpress-bbhbdhdqebdqf9a3.eastus-01.azurewebsites.net',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Aplicaciones.Trabajo.middleware.UserActivityMiddleware'
]

ROOT_URLCONF = 'Ali.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Ali.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Alifrut2',
        'USER': 'Edgar664',
        'PASSWORD':'Bared664',
        'PORT':'3306',
        'HOST':"alifrut2024.mysql.database.azure.com"
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ 
    'Aplicaciones/Trabajo/static',
    "Aplicaciones/Trabajo/static",
    "Aplicaciones/Calidad/static", 
    "Aplicaciones/Produccion/static",
    "Aplicaciones/Recepcion/static"
    ]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL='Trabajo.Usuario'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Backend de autenticación predeterminado
)

LOGIN_URL = '/login/'  # URL de inicio de sesión
LOGOUT_URL = '/logout/'  # URL de cierre de sesión
