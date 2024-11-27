import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from about.models import Curriculum, Contact, Prestation, Presentation, Gallerie
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestAboutIntegration(TestCase):
    def setUp(self):
        # Créer un client de test
        self.client = Client()
        
        # Créer un utilisateur de test
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        
        # Créer un curriculum de test
        self.curriculum = Curriculum.objects.create(
            nom="John Doe",
            description="<p>Développeur Full Stack</p>",
            photo=SimpleUploadedFile(
                name='test_photo.jpg',
                content=b'',
                content_type='image/jpeg'
            ),
            cv=SimpleUploadedFile(
                name='test_cv.pdf',
                content=b'',
                content_type='application/pdf'
            )
        )
        
        # Créer un contact de test
        self.contact = Contact.objects.create(
            nom="Jane Doe",
            email="jane@example.com",
            subject="Test Subject",
            telephone=123456789,
            message="Test message"
        )
        
        # Créer une prestation de test
        self.prestation = Prestation.objects.create(
            titre="Service Test",
            description="Description du service test",
            image=SimpleUploadedFile(
                name='test_image.jpg',
                content=b'',
                content_type='image/jpeg'
            )
        )

    def test_curriculum_creation(self):
        # Tester la création d'un curriculum
        curriculum = Curriculum.objects.get(nom="John Doe")
        self.assertEqual(curriculum.description, "<p>Développeur Full Stack</p>")
        self.assertTrue(curriculum.status)

    def test_contact_creation_and_update(self):
        # Tester la création et la mise à jour d'un contact
        contact = Contact.objects.get(email="jane@example.com")
        self.assertEqual(contact.nom, "Jane Doe")
        
        # Tester la mise à jour
        contact.subject = "Updated Subject"
        contact.save()
        updated_contact = Contact.objects.get(pk=contact.pk)
        self.assertEqual(updated_contact.subject, "Updated Subject")

    def test_prestation_creation_and_deletion(self):
        # Tester la création d'une prestation
        prestation = Prestation.objects.get(titre="Service Test")
        self.assertEqual(prestation.description, "Description du service test")
        
        # Tester la suppression
        initial_count = Prestation.objects.count()
        prestation.delete()
        self.assertEqual(Prestation.objects.count(), initial_count - 1)

    def test_multiple_models_interaction(self):
        # Tester les interactions entre plusieurs modèles
        self.assertEqual(Curriculum.objects.count(), 1)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Prestation.objects.count(), 1)
        
        # Vérifier que tous les modèles sont actifs (status=True)
        self.assertTrue(all(model.status for model in Curriculum.objects.all()))
        self.assertTrue(all(model.status for model in Contact.objects.all()))
        self.assertTrue(all(model.status for model in Prestation.objects.all()))

    