from django.test import SimpleTestCase
from django.urls import reverse

# create a simple test for the home page
class HomePageTests(SimpleTestCase):

    # check if url exists at the correct location
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

    def test_template_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')
        self.assertContains(response,"Home")
