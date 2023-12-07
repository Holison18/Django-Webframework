from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
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

# create a view to update blog post
class UpdateBlogView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title","body"]

# creat a view to delete blog post
class DeleteBlogView(DeleteView):
    model = Post
    template_name = "post_delete.html"