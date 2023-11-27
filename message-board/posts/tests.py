from django.test import TestCase
from django.urls import reverse

# import model
from .models import Post


# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(text="This is just a text")

    # tesf for model content
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is just a text")

    # test if url exist at location
    def test_url_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # home page unit tests
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "<h1>Message Board Home Page</h1>")
        
