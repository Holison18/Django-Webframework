from django.views.generic import CreateView
from .forms import UserCreationForm
from django.urls import reverse_lazy

# create a view for signup
class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'signup.html'
