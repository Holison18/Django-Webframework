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
        self.assertEqual(response.status_code,200)


# create a test for the about page
class aboutPageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
