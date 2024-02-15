"""
Django settings for SocialWebsite project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q6bbq+)5t&^r++8g67o6)(zpxsm_y_=5!%(qt^6tg9@(mzxk@s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# this is needed to be added for media
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

LOGIN_URL = 'a_ccount:login_view'
LOGOUT_URL = 'a_ccount:logout_view'
LOGIN_REDIRECT_URL = "a_ccount:dashboard_view"
# configuring facebook
# SOCIAL_AUTH_FACEBOOK_KEY = '344593331762062'
# SOCIAL_AUTH_FACEBOOK_SECRET = "56bd8b4137815825d7628c05ac125c4b"
# SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
# Application definition
# AUTH_USER_MODEL = 'a_ccount.bookmarker'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTHENTICATION_BACKENDS = [
    # if any of these authenticated, stop and login
    'a_ccount.custom_authentication_backends.EmailAuthentication',
    'a_ccount.custom_authentication_backends.LastNameAuthentication',
    'django.contrib.auth.backends.ModelBackend',
    "allauth.account.auth_backends.AuthenticationBackend",
    # "social_core.backends.facebook.FacebookOAuth2",
]
ACCOUNT_EMAIL_VERIFICATION = "none"
INSTALLED_APPS = [
    # 'a_ccount.apps.AppConfig',
    # "oauth2_provider",
    'action.apps.ActionConfig',
    'peopel.apps.PeopelConfig',
    "images.apps.ImageConfig",
    "easy_thumbnails.apps.EasyThumbnailsConfig",
    'a_ccount.apps.a_ccountConfig',  # if this is the first, means engine will first search here for templates
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",
    "django.contrib.sites",  # added for allauth needs
    # 3rd party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # social provider
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SocialWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'tempaltes')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # for social auth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# print(TEMPLATES[0]['DIRS'])

WSGI_APPLICATION = 'SocialWebsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sapp',
        'USER': 'facebooker',
        'PASSWORD': 'Zawar@123',
        'HOST': 'localhost',
        'PORT': 5432
    }
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
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': '0b02ce2706adb449f42f',
            'secret': 'd29d532e1d63fa096895037b17d18c19fd35929b',
        },

        'facebook': {
            'APP': {
                'client_id': '344593331762062',
                "secret": '56bd8b4137815825d7628c05ac125c4b'
            }
        },
        # should run on https://127.0.0.1:8080
        # no changed to https://www.mysite.com:8080/a_ccount
        'google': {
            'APP': {
                'client_id': "468975016235-jf7c6ang7ip33l441ggg54jqg45lt7hl.apps.googleusercontent.com",
                'secret': "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"
            }
        }

    }
}

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda user: reverse_lazy('a_ccount:user_details',args=[user.username]),
}
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SESSION_COOKIE_AGE = 600
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "tareeqshah5@gmail.com"
EMAIL_HOST_PASSWORD = "bedz djgn edvf upzg"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# for social authentication
# SITE_ID = 10 # https://127.0.0.1:8080 # google and github
# SITE_ID = 7  # https:www.mysite.com:8080 # facebook
SITE_ID = 8  # https://www.mystite.com:8080/a_ccount/
# from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

if DEBUG:
    import mimetypes
    mimetypes.add_type('application/javascript', '.js', True)
    mimetypes.add_type('text/css', '.css', True)
