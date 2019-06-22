from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):


    def test_create_user_with_email_success(self):
        email = "nishantsaarf20@gmail.com"
        password = "test1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_for_normalize_email(self):
        email = "nishant@FJEICKN.com"
        user = get_user_model().objects.create_user(email, "2244r3d")
        self.assertEqual(user.email, email.lower())

    def test_for_email_validation(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12w2edd')

    def test_for_superuser(self):
        user = get_user_model().objects.create_superuser(
            'n@gmil.com',
            '1223ed'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
