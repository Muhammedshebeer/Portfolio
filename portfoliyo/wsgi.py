import os
import sys

# Add your project directory to the sys.path
project_home = '/home/mhdshabeer/Portfoliyo-main/portfoliyo'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfoliyo.settings'

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
