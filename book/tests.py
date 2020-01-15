from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Data


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.data = Data.objects.create(
            title='A good title',
            about='Nice body content',
            author='Name',
            user=self.user,
        )

    def test_string_representation(self):
        data = Data(title='A sample title')
        self.assertEqual(str(data), data.title)

    def test_post_content(self):
        self.assertEqual(f'{self.data.title}', 'A good title')
        self.assertEqual(f'{self.data.user}', 'testuser')
        self.assertEqual(f'{self.data.about}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'list_view.html')

    def test_post_detail_view(self):
        response = self.client.get('/detail/1/')
        no_response = self.client.get('/detail/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'detail_view.html')
