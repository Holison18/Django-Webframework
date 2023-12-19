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
            
        )