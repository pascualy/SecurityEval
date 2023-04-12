def define_database():
    DATABASE = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'database_name',
            'USER': 'database_user',
            'PASSWORD': 'database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

    return DATABASE