from django.urls import path 
from .views import ArticleListView
# url patterns
urlpatterns = [
    path("",ArticleListView.as_view(),name="article_list")
]