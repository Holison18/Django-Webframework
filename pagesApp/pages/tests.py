from django.test import SimpleTestCase
from django.urls import reverse


# test for homepage
class homePageTests(SimpleTestCase):
    # url test
    def urls_successful_test(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # url name available test
    def test_url_name_available(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # check html template
    def test_template_name_available(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    # check template content
    def test_template_content(self):
        response = self.client.get("home")
        self.assertContains(response, "<h1>Home Page</h1>")

    # about page test
    class aboutPageTests(SimpleTestCase):
        # url test
        def urls_successful_test(self):
            response = self.client.get("/about/")
            self.assertEqual(response.status_code, 200)

        # url name available test
        def test_url_name_available(self):
            response = self.client.get(reverse("about"))
            self.assertEqual(response.status_code, 200)

        # check html template
        def test_template_name_available(self):
            response = self.client.get(reverse("about"))
            self.assertTemplateUsed(response, "about.html")

        # check template content
        def test_template_content(self):
            response = self.client.get("about")
            self.assertContains(response, "<h1>About Page</h1>")
