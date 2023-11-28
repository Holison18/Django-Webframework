from django.test import TestCase
from django.urls import reverse
from .models import Post

# create a test for the posts app
class PostTtests(TestCase):

    # create a temporary data base using setUpTestData function
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text = "Testing Text")

    # test if database works correctly
    def test_model_available(self):
        self.assertEqual(self.post.text, "Testing Text")

    # check if url exist at the correct location
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # create a unit text for homepage
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "<h1>Message Board Home Page</h1>")