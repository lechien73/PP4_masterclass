from django.shortcuts import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username="test", password="test", email="test@test.com")
        self.post = Post(title="Test post", author=self.user, slug="test", \
                         excerpt="Test excerpt", content="Test content", status=1)
        self.post.save()

    def test_get_post_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_get_post(self):
        response = self.client.get(reverse('post_detail', args=['test']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_like(self):
        self.client.login(username='test', password='test')
        self.client.post(reverse('post_like', args=['test']))
        post = Post.objects.filter(slug='test').first()
        self.assertEqual(post.number_of_likes(), 1)
    
    def test_unlike(self):
        self.client.login(username='test', password='test')
        self.client.post(reverse('post_like', args=['test']))
        self.client.post(reverse('post_like', args=['test']))
        post = Post.objects.filter(slug='test').first()
        self.assertEqual(post.number_of_likes(), 0)
    
    def test_comment(self):
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('post_detail', args=['test']), {
            'body': 'This is a test comment'
        })
        self.assertEqual(response.context['commented'], True)
