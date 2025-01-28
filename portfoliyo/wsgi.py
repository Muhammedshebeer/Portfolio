import os
import sys

# Set the project base directory
project_home = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add project directory to the Python path
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfoliyo.settings")

# Get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

