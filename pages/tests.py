from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.resp = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.resp,'home.html')

    def test_homepage_contains(self):
        self.assertContains(self.resp, "Home Page")

    def test_homepage_not_contains(self):
        self.assertNotContains(self.resp, "No more bugs todat :P")

    def test_homepage_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.resp = self.client.get(url)
    
    def test_about_page_status_code(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.resp, 'about.html')

    def test_about_page_contains_html(self):
        self.assertContains(self.resp, 'About Page')

    def test_about_page_does_not_contain(self):
        self.assertNotContains(self.resp, 'Invalid Text')

    def test_about_page_resolve_view(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
