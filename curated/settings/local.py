from .base import *

WAGTAILADMIN_BASE_URL = 'localhost'

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

INTERNAL_IPS = ["127.0.0.1"]

# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

UMAMI_KEY = os.environ.get("UMAMI_KEY")
UMAMI_ADDRESS = os.environ.get("UMAMI_ADDRESS")