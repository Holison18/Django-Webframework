from django.views.generic import TemplateView

# create a template view for the homepage
class HomePageView(TemplateView):
    template_name = 'home.html'