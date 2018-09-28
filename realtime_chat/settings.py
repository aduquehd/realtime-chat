import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'wm$u3)1v!p*-nutpjpn+&%f94r$i3&*dm)jyuba4v379yqlgi('

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Created apps
    'apps.authentication',
    'apps.chat',
    'apps.shared',

    # Installed apps
    'channels',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'realtime_chat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'realtime_chat.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/chat/rooms'
LOGOUT_REDIRECT_URL = '/accounts/login'

# Django channels
ASGI_APPLICATION = "realtime_chat.routing.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Database setup
if os.environ.get("ENVIRONMENT_NAME") in ("PRODUCTION",):
    SECRET_KEY = os.environ["REALTIME_CHAT_SECRET_KEY"]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    DEBUG = False

    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': os.environ['REALTIME_CHAT_DB_ENGINE'],
            'NAME': os.environ["REALTIME_CHAT_DB_NAME"],
            'HOST': os.environ["REALTIME_CHAT_DB_HOST"],
            'PORT': os.environ["REALTIME_CHAT_DB_PORT"],
            'USER': os.environ["REALTIME_CHAT_DB_USER"],
            'PASSWORD': os.environ["REALTIME_CHAT_DB_PASSWORD"],
        }
    }
else:
    from .database_info import NAME, HOST, PORT, USER, PASSWORD, ENGINE

    SECRET_KEY = 'o353m1235nje=65!+rhz-asdf1241f5&&&ns@_rye(i(5sin9yo$2346234x=sf9ate@k'

    DEBUG = True

    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': ENGINE,
            'NAME': NAME,
            'HOST': HOST,
            'PORT': PORT,
            'USER': USER,
            'PASSWORD': PASSWORD,
            'TEST': {
                'NAME': "test_{}".format(NAME)
            }
        }
    }
