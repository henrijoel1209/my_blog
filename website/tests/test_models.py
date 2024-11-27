"""
Tests des modèles pour l'application website
"""
import pytest
from django.test import TestCase
from django.core.exceptions import ValidationError
from website.models import SiteInfo, SocialCount, Newsletter
from django.core.files.uploadedfile import SimpleUploadedFile

class WebsiteSiteInfoTest(TestCase):
    def setUp(self):
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Test Site",
            telephone=123456789,
            description="Test description",
            logo=SimpleUploadedFile("test_logo.jpg", b"file_content")
        )

    def test_site_info_creation(self):
        self.assertEqual(self.site_info.email, "test@example.com")
        self.assertEqual(self.site_info.nom, "Test Site")
        self.assertEqual(self.site_info.telephone, 123456789)
        self.assertEqual(self.site_info.description, "Test description")
        self.assertTrue(self.site_info.status)

    def test_site_info_str_method(self):
        self.assertEqual(str(self.site_info), "Test Site")

class WebsiteSocialCountTest(TestCase):
    def setUp(self):
        self.social = SocialCount.objects.create(
            nom="Facebook",
            lien="https://facebook.com",
            icones="facebook"
        )

    def test_social_count_creation(self):
        self.assertEqual(self.social.nom, "Facebook")
        self.assertEqual(self.social.lien, "https://facebook.com")
        self.assertEqual(self.social.icones, "facebook")
        self.assertTrue(self.social.status)

    def test_invalid_icone_choice(self):
        with self.assertRaises(ValidationError):
            social = SocialCount(
                nom="Invalid",
                lien="https://example.com",
                icones="invalid_icon"
            )
            social.full_clean()

class WebsiteNewsletterTest(TestCase):
    def setUp(self):
        self.newsletter = Newsletter.objects.create(
            email="subscriber@example.com"
        )

    def test_newsletter_creation(self):
        self.assertEqual(self.newsletter.email, "subscriber@example.com")
        self.assertTrue(self.newsletter.status)

    def test_invalid_email(self):
        with self.assertRaises(ValidationError):
            newsletter = Newsletter(email="invalid-email")
            newsletter.full_clean()

    def test_null_email(self):
        newsletter = Newsletter.objects.create(email=None)
        self.assertIsNone(newsletter.email)
