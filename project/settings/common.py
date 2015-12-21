"""
common specific project settings
"""
from settings.common import *  # noqa
from heroku_env import env, cast_bool


INSTALLED_APPS += (
    'userena',
    'guardian',
    'easy_thumbnails',
    'accounts',
)


AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)


ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.MyProfile'


USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

USERENA_USE_HTTPS = env('USERENA_USE_HTTPS', cast=cast_bool, default=False)
