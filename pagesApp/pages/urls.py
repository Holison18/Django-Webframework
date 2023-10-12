from django.urls import path
from .views import HomePageView, About, Contact


urlpatterns = [
    path("contact/", Contact.as_view(), name="contactUs"),
    path("about/", About.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
