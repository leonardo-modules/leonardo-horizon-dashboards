
from __future__ import absolute_import

import horizon_contrib

from horizon import Horizon
from django.conf.urls import include, url

urlpatterns = [

    url(r'', include(Horizon._lazy_urls)),
    url(r'', include(horizon_contrib.urls)),

]
