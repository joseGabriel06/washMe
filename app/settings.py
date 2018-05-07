import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = True

#smtp server settings for gmail
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_USER     = 'ecd.536.washme1@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD'] 
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True

ALLOWED_HOSTS = ['*']

DJANGO_CORE_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

CORE_APPS = (
    'homepage',
    'washer',  
)

THIRD_PATTY_APPS = (
    'registration',
    'widget_tweaks',
    'material',
    'material.frontend',
    'material.admin',
    'crispy_forms',
    'social_django',  # <--
)

INSTALLED_APPS = DJANGO_CORE_APPS + THIRD_PATTY_APPS + CORE_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',  # <--
]

ROOT_URLCONF = 'app.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
            'loaders': [
                # PyPugJS part:   ##############################
                ('pypugjs.ext.django.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ))
            ],
            'builtins': ['pypugjs.ext.django.templatetags'],  # Remove this line for Django 1.8
        },
    },

]


WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':os.environ['DATABASE_NAME'], 
        'USER':os.environ['DATABASE_USER'],
        'PASSWORD':os.environ['DATABASE_PASSWORD'],
        'HOST':os.environ['DATABASE_HOST'],
        'PORT': 5432,
        'CHARSET':'UTF8',
    }
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)


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


LANGUAGE_CODE = 'es-co'

TIME_ZONE     = 'America/Bogota'

USE_I18N      = True

USE_L10N      = True

USE_TZ        = True


STATIC_URL = '/static/'
MEDIA_URL  = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_ROOT = os.path.join((BASE_DIR), "venv","static_env","static_root")
MEDIA_ROOT = os.path.join((BASE_DIR),  "venv","static_env","media_root")

SITE_ID                 =1
REGISTRATION_FORM_PATH  = 'myapp.forms.CustomForm'
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.
SITE_ID                 = 1
LOGIN_REDIRECT_URL      ='pay'

LOGOUT_URL = 'home'


SOCIAL_AUTH_TWITTER_KEY    = 'GZRLBBOz845n9awPAKgHTNbSa'
SOCIAL_AUTH_TWITTER_SECRET = 'N8u5LdLV9vdC4NHw3RZ14MuV0D9syHo77MBh4Nc0oUsvBTTlU7'


SOCIAL_AUTH_FACEBOOK_KEY = '290742108111390'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '5d373c5ca4de643d68d80a7f7ada87be'  # App Secret

