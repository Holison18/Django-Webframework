from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model


# signup page tests
class SignupPageTests(TestCase):
    # test if the url exists at the correct location
    def test_if_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    # test if the view name exists
    def test_view_name_exists(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    # test if the forms works correct
    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testusername",
                "email": "testemail@email.com",
                "password1": "mytest123",
                "password2": "mytest123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testusername")
        self.assertEqual(get_user_model().objects.all()[0].email, "testemail@email.com")
