from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser3",
                "email": "testuser3@test3.com",
                "password1": "testuser3password",
                "password2": "testuser3password",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser3")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser3@test3.com")
