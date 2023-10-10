from django.urls import path
from .views import HomePageView, About


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("", About.as_view(), name="about"),
]
