from .base import *
import dj_database_url

DEBUG = False

INSTALLED_APPS += [
    'whitenoise.runserver_nostatic',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': os.environ.get("CLOUDINARY_API_KEY"),
    'API_SECRET': os.environ.get("CLOUDINARY_API_SECRET")
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Ensure CSRF_TRUSTED_ORIGINS includes a valid domain, and fallback to localhost if none provided.
HOST_NAME = os.environ.get("HOST_NAME", None)  # Ensure this is set in your environment

if HOST_NAME:
    CSRF_TRUSTED_ORIGINS = [
        'https://*.127.0.0.1',  # Allow local development
        f'https://{HOST_NAME}',  # Dynamic host name from environment
    ]
else:
    # Fallback for local development
    CSRF_TRUSTED_ORIGINS = [
        'http://localhost:8000',
        'http://127.0.0.1:8000',
    ]
