from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secrete"
        )

        cls.post = Post.objects.create(title="Title", body="Body", author=cls.user)

    def test_post_model(self):
        self.assertEqual(self.post.title, "Title")
        self.assertEqual(self.post.body, "Body")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "Title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_if_url_location_exists_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_if_url_location_exists_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_listview(self):
        response1 = self.client.get(reverse("home"))
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed(response1, "home.html")
        self.assertContains(response1, "Body")

    def test_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "post_detail.html")
        self.assertContains(response, "Title")

    def test_createView(self):
        response = self.client.post(
            reverse(
                "post_new",
            ),
            {"title": "New Title", "body": "body", "author": self.user.id},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New Title")
        self.assertEqual(Post.objects.last().body, "body")

    def test_post_updateView(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {"title": "Updated title", "body": "Updated Body"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated Body")

    def test_deleteView(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
