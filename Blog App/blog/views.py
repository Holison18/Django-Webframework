from django.views.generic import ListView
from .models import Post

# create a view for the home page
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
