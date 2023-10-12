from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"

class contactUs(TemplateView):
    template_name = "contactUs.html"