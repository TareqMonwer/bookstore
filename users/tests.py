from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


class CustomUserTest(TestCase):

    def test_user_create(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            password='321nop4a55',
            email='testuser@nomail.com'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='super',
            password='n0p4s5w0rd',
            email='super@man.marvel'
        )
        self.assertEqual(admin_user.username, 'super')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        


class SignupPageTest(TestCase):
    username = 'testuser'
    email = 'testemail@gmail.com'
    def setUp(self):
        url = reverse('account_signup')
        self.resp = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.resp.status_code, 200)
        self.assertContains(self.resp, 'Create New Account')
        self.assertNotContains(self.resp, 'Go away')
        self.assertTemplateUsed('accounts/signup.html')
    
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)