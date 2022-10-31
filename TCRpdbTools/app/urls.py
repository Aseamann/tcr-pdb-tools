from django.urls import path

from app.views import (
    home_redirect_view,
    pdb_tools_view,
    post_pdb_view,
)

urlpatterns = [
    path("", home_redirect_view, name="home_redirect"),
    path("pdb-tools/", pdb_tools_view, name="pdb_form"),
    path("pdb-tools/post-pdb/", post_pdb_view, name="post_pdb"),
]
