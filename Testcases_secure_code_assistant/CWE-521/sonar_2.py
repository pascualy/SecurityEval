
# Import necessary modules
import os

# Define the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the DATABASES dictionary
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',   # Choose your database engine
        'NAME': 'mydatabase',   # Replace with your database name
        'USER': 'mydatabaseuser',   # Replace with your database username
        'PASSWORD': 'mypassword',   # Replace with your database password
        'HOST': 'localhost',   # Replace with your database host
        'PORT': '5432',   # Replace with your database port
    }
}

# Set the DATABASES variable in the settings
settings.DATABASES = DATABASES
