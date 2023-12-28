from django.urls import path 
from .views import ArticleListView,ArticleDetailView,ArticleUpdateView,ArticleDeleteView
# url patterns
urlpatterns = [
    path("<int:pk>/",ArticleDetailView.as_view(),"article_detail"),
    path("<int:pk>/edit/",ArticleUpdateView.as_view(),"article_edit"),
    path("<int:pk>/delete/",ArticleDeleteView.as_view(),"article_delete"),
    path("",ArticleListView.as_view(),name="article_list")
]