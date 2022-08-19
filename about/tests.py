from django.test import TestCase
from django.shortcuts import reverse


class TestView(TestCase):

    def test_get_about(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
