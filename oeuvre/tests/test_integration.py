import pytest
from django.test import TestCase, Client
from django.urls import reverse
from oeuvre.models import Poesie
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestPoesieIntegration(TestCase):
    def setUp(self):
        # Créer un utilisateur pour les tests
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        # Créer quelques poésies pour les tests
        self.poesie1 = Poesie.objects.create(
            titre="Premier poème",
            description="Description du premier poème",
            poeme="<p>Contenu du premier poème</p>"
        )
        self.poesie2 = Poesie.objects.create(
            titre="Deuxième poème",
            description="Description du deuxième poème",
            poeme="<p>Contenu du deuxième poème</p>"
        )

    def test_liste_poesies(self):
        # Tester que toutes les poésies sont dans la base de données
        poesies = Poesie.objects.all()
        self.assertEqual(poesies.count(), 2)
        self.assertIn(self.poesie1, poesies)
        self.assertIn(self.poesie2, poesies)

    def test_detail_poesie(self):
        # Tester la récupération d'une poésie spécifique
        poesie = Poesie.objects.get(titre="Premier poème")
        self.assertEqual(poesie.description, "Description du premier poème")
        self.assertEqual(poesie.poeme, "<p>Contenu du premier poème</p>")

    def test_modification_poesie(self):
        # Tester la modification d'une poésie
        self.poesie1.description = "Nouvelle description"
        self.poesie1.save()
        poesie_modifiee = Poesie.objects.get(pk=self.poesie1.pk)
        self.assertEqual(poesie_modifiee.description, "Nouvelle description")

    def test_suppression_poesie(self):
        # Tester la suppression d'une poésie
        self.poesie1.delete()
        poesies = Poesie.objects.all()
        self.assertEqual(poesies.count(), 1)
        self.assertNotIn(self.poesie1, poesies)
