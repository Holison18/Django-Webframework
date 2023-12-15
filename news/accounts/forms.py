from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomCreationForm(UserCreationForm):
    model = CustomUser
    fields = UserCreationForm.Meta.fields + ("age",)