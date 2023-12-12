from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/",include("django.contrib.auth.urls")), # new
    path("accounts/",include("accounts.url")), # new
    path("",include("blog.urls")), # new
]