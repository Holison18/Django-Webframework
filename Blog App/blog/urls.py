from django.urls import path
from .views import BlogListView,BlogDetailView,CreateBlogView,UpdateBlogView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"), #home
    path("post/<int:pk>/",BlogDetailView.as_view(),name="post_detail"),
    path("post/new/",CreateBlogView.as_view(),name="post_new"),
    path("post/new/",UpdateBlogView.as_view(),name="post_update"),
]
