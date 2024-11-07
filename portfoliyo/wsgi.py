import os
import sys

# Add the project directory to the sys.path
project_path = '/home/muhdshabeer/portfoliyo'
if project_path not in sys.path:
    sys.path.append(project_path)

# Set the environment variable for the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'yourprojectname.settings'

# Activate the virtual environment
activate_env = os.path.expanduser('/home/yourusername/.virtualenvs/myenv/bin/activate_this.py')
with open(activate_env) as f:
    exec(f.read(), dict(__file__=activate_env))

# Import Django's WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
