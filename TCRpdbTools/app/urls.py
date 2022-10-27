from django.urls import path

from app.views import (
    home_redirect_view,
    simple_form_view,
    post_form_view,
    test_markdownify,
    pdb_tools_view,
)

urlpatterns = [
    path("", home_redirect_view, name="home_redirect"),
    path("simple-form/", simple_form_view, name="simple_form"),
    path("pdb-tools/", pdb_tools_view, name="pdb_form"),
    path("post-form/", post_form_view, name="post_form"),
    path("test-markdownify/", test_markdownify, name="test_markdownify"),
]
