from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("articles/",include("articles.urls")), # added url path for articles app
    path("", include("pages.urls")), # added url paths to pages app
]
