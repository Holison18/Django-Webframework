from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


# create a class for detailView
class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ["title","Body"]