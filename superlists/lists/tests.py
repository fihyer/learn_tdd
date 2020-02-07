from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

    def test_homepage_returns_corret_html(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

