"""
Tests d'intégration pour l'application website
"""
import pytest
from django.test import TestCase, Client
from django.urls import reverse
from website.models import SiteInfo, SocialCount, Newsletter
from django.core.files.uploadedfile import SimpleUploadedFile

class WebsiteIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Créer des données de test
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Test Site",
            telephone=123456789,
            description="Test description",
            logo=SimpleUploadedFile("test_logo.jpg", b"file_content")
        )
        
        self.social_count = SocialCount.objects.create(
            nom="Facebook",
            lien="https://facebook.com",
            icones="facebook"
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')
        self.assertIn('site_info', response.context)
        
    def test_newsletter_subscription(self):
        response = self.client.post(
            reverse('is_newsletter'),
            {'email': 'test@example.com'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Newsletter.objects.filter(email='test@example.com').exists())
        
    def test_invalid_newsletter_subscription(self):
        response = self.client.post(
            reverse('is_newsletter'),
            {'email': 'invalid-email'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Newsletter.objects.filter(email='invalid-email').exists())

    def test_navigation(self):
        """Test de navigation entre les pages du site"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    