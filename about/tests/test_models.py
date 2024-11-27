import pytest
from django.test import TestCase
from about.models import Curriculum, Contact, Prestation, Presentation, Gallerie
from django.core.files.uploadedfile import SimpleUploadedFile

class TestCurriculumModel(TestCase):
    def setUp(self):
        self.curriculum = Curriculum.objects.create(
            nom="Test Curriculum",
            description="Test Description",
            photo=SimpleUploadedFile("test_photo.jpg", b"file_content"),
            cv=SimpleUploadedFile("test_cv.pdf", b"file_content")
        )

    def test_curriculum_creation(self):
        self.assertEqual(self.curriculum.nom, "Test Curriculum")
        self.assertEqual(self.curriculum.description, "Test Description")
        self.assertTrue(self.curriculum.status)

class TestContactModel(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            nom="Test Contact",
            email="test@example.com",
            subject="Test Subject",
            telephone=123456789,
            message="Test Message"
        )

    def test_contact_creation(self):
        self.assertEqual(self.contact.nom, "Test Contact")
        self.assertEqual(self.contact.email, "test@example.com")
        self.assertEqual(self.contact.subject, "Test Subject")
        self.assertEqual(self.contact.telephone, 123456789)
        self.assertEqual(self.contact.message, "Test Message")

class TestPrestationModel(TestCase):
    def setUp(self):
        self.prestation = Prestation.objects.create(
            titre="Test Prestation",
            description="Test Description",
            image=SimpleUploadedFile("test_image.jpg", b"file_content")
        )

    def test_prestation_creation(self):
        self.assertEqual(self.prestation.titre, "Test Prestation")
        self.assertEqual(self.prestation.description, "Test Description")
        self.assertTrue(self.prestation.status)

class TestPresentationModel(TestCase):
    def setUp(self):
        self.presentation = Presentation.objects.create(
            titre="Test Presentation",
            description="Test Description",
            image=SimpleUploadedFile("test_image.jpg", b"file_content")
        )

    def test_presentation_creation(self):
        self.assertEqual(self.presentation.titre, "Test Presentation")
        self.assertEqual(self.presentation.description, "Test Description")
        self.assertTrue(self.presentation.status)

class TestGallerieModel(TestCase):
    def setUp(self):
        self.gallerie = Gallerie.objects.create(
            titre="Test Gallerie",
            gallerie=SimpleUploadedFile("test_image.jpg", b"file_content")
        )

    def test_gallerie_creation(self):
        self.assertEqual(self.gallerie.titre, "Test Gallerie")
        self.assertTrue(self.gallerie.status)
