from django.urls import path
from .views import BlogListView,BlogDetailView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"), #home
    path("post_details",BlogDetailView.as_view(),name="post_details")
]
