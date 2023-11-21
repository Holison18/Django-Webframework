from django.views.generic.base import TemplateView


# create a template view for the homepage
class homePageView(TemplateView):
    template_name = "home.html"

# create a template view for the about page
class aboutPageView(TemplateView):
    template_name = "about.html"
