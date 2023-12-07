from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .models import Post

# create a view for the home page
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

# create a detailed view class for blog posts
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

# create a new blog post view
class CreateBlogView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title","author","body"]