import os
import sys

# Add your project directory to the sys.path
project_home = '/home/mhdshabeer/Portfoliyo-main/portfoliyo'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfoliyo.settings'

# Activate the virtual environment
activate_this = '/home/mhdshabeer/Portfoliyo-main/portfoliyo/myvenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), {'__file__': activate_this})

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
