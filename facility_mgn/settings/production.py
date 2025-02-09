# from google.oauth2 import service_account
from .base import *
from .dbconf import POSTGRESDB, MANGODB

"""Production Ready Settings
"""

TEMP_SECRET_KEY = "srt@v69cp$hm2^g-z#m%n18pl(+*mmx6+tl$t^s9h55%1v%*it"
SECRET_KEY = os.environ.get("SECRET_KEY", TEMP_SECRET_KEY)
DEBUG = False

ALLOWED_HOSTS += [
    "facility_mgn.dabolinux.com",
    "www.facility_mgn.dabolinuxcom",
    "facility_mgn.chinikiguard.com",
    "www.facility_mgn.chinikiguard",
    "facility_mgnadmin.chinikiguard.com",
    "www.facility_mgnadmin.chinikiguard",
    "facility_mgn.com.ng",
    "www.facility_mgn.com.ng",
]

# CSRF_TRUSTED_ORIGINS Required in Django 4.0
# CSRF_TRUSTED_ORIGINS = []

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

DATABASES = POSTGRESDB
# DATABASES = MANGODB


STATIC_ROOT = os.path.join(PROJECT_ROOT, "staticfiles")
STATIC_URL = "/facility_mgnstatic/"
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "static"),)
MEDIA_URL = "/facility_mgnmedia/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")


# Google cloud for images
#DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# GS_PROJECT_ID = 'tquaters'
# GS_BUCKET_NAME = 'tquaters_bucket'
# GS_FILE_OVERWRITE = True
# GS_LOCATION = 'tquaters/tquaters'
# GS_AUTH_FILE = os.path.join(PROJECT_ROOT, "tquaters-65696f642f71.json")
# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#     GS_AUTH_FILE)
