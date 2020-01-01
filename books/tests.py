from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase, Client
from django.urls import reverse

from .models import Book, Review


class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='djtest',
            email='djtest@mail.com',
            password='hellodj123',
        )
        self.pro = Permission.objects.get(codename='standard_pack')

        self.book = Book.objects.create(title='Think Python',
            author='Allen B. Downey',
            price='20.99',
        )

        self.review = Review.objects.create(
            book=self.book,
            review='Nice One From Test',
            author=self.user,
        )
        
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Think Python')
        self.assertEqual(f'{self.book.author}', 'Allen B. Downey')
        self.assertEqual(f'{self.book.price}', '20.99')

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email='djtest@mail.com', password='hellodj123')
        resp = self.client.get(reverse('book-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Think Python')
        self.assertTemplateUsed(resp, 'books/book_list.html')
    
    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        resp = self.client.get(reverse('book-list'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp,
            '%s?next=/books/' % (reverse('account_login'))
        )
        resp = self.client.get('%s?next=/books/' % (reverse('account_login')))
        self.assertContains(resp, 'User Login')
    
    def test_book_detail_view_for_permitted_user(self):
        self.client.login(email='djtest@mail.com', password='hellodj123')
        self.user.user_permissions.add(self.pro)
        resp = self.client.get(self.book.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
        no_resp = self.client.get('/books/123/')
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, 'Think Python')
        self.assertContains(resp, 'Nice One From Test')
        self.assertTemplateUsed(resp, 'books/book_detail.html')