from django.test import SimpleTestCase
from django.urls import reverse


# create a class for HomePage tests
class homePageTests(SimpleTestCase):
    # url successful test
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # url name test
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # check if the html template name is correct
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    # check template content is correct
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response,"<h1>Home Page</h1>")


# create a class for About Page tests
class aboutPageTests(SimpleTestCase):
    # url successful test
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    # url name test
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    # check if the html template name is correct
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    # check template content is correct
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response,"<h1>About Page</h1>")
