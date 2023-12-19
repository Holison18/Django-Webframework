from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class SignupPageTests(TestCase):
    # test if url exist at the correct location
    def test_url_exits_at_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code,200)

    # test if view name exist
    def test_view_name_exits(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testusername",
                "email": "test@email.com",
                "password1": "mytest123",
                "password2": "mytest123",
            }
        )
        self.assertEqual(response.status_code,302)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,"testusername")
        self.assertEqual(get_user_model().objects.all()[0].email,"test@email.com")