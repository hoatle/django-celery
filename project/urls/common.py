"""
project specific settings for urls in common
"""

from urls.common import *  # noqa

urlpatterns += (
    url(r'^accounts/', include('userena.urls')),
)
