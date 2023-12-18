from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


# create a view for signup
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
