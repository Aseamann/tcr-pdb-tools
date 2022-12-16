from django.urls import re_path, include

#Django Rest Framework
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from api import controllers
from django.views.decorators.csrf import csrf_exempt

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    re_path(r'^pdbs', csrf_exempt(controllers.PdbList.as_view())),
    re_path(r'^actions', csrf_exempt(controllers.ActionList.as_view())),
    re_path(r'^fetchpdb', csrf_exempt(controllers.FetchPdb.as_view())),
    re_path(r'^tcrrequest/(?P<pk>[0-9]+)$', csrf_exempt(controllers.TcrRequestDetail.as_view())),
    re_path(r'^tcrrequest', csrf_exempt(controllers.TcrRequestList.as_view())),
    re_path(r'^', include(router.urls)),
]
