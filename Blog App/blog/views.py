from django.views.generic import ListView,DetailView
from .models import Post

# create a view for the home page
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

# create a detailed view class for blog posts
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"