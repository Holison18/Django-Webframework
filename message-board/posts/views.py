from django.views.generic import ListView
from .models import Post

# create a Listview for our homepage
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
