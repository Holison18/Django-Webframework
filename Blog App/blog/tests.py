from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post


# Create your tests here.
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            name="testuser", email="test@email.com", password="secrete"
        )

        cls.post = Post.objects.create(title="Title", body="Body", author=cls.user)

    def test_post_model(self):
        self.assertEqual(self.post.title,"Title")
        self.assertEqual(self.post.body,"Body")
        self.assertEqual(self.post.author.username,"testuser")
        self.assertEqual(str(self.post),"Title")
        self.assertEqual(self.post.get_absolute_url(),"/post/1/")
