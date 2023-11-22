from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


# create a test for the homepage
class homePageTests(SimpleTestCase):
    # test if url returns successfully
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # test to see if url name returns successfully
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # test template name
    def test_template_name_available(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")


# create a test for the about page
class aboutPageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    # test to see if url name returns successfully
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    # test template name available
    def test_template_name_available(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "about.html")
