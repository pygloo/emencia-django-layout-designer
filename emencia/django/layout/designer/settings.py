"""Settings for edn layout designer module.
"""

# python import
import os

# django import
from django.conf import settings

# specific media url for edld
MEDIA_URL = settings.MEDIA_URL + 'edld/'

# specific media url for edld
MEDIA_ROOT = os.path.join(settings.MEDIA_ROOT, 'edld')

