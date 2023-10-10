from django.urls import path
from .views import HomePageView, About


urlpatterns = [
    path("about/", About.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
