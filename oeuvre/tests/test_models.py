import pytest
from django.test import TestCase
from oeuvre.models import Poesie
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
import time

@pytest.mark.django_db
class TestPoesieModel(TestCase):
    def setUp(self):
        # Créer une instance de poésie pour les tests
        self.poesie = Poesie.objects.create(
            titre="Test Poème",
            description="Une description de test",
            poeme="<p>Contenu du poème de test</p>"
        )

    def test_poesie_creation(self):
        # Tester la création d'une poésie
        self.assertEqual(self.poesie.titre, "Test Poème")
        self.assertEqual(self.poesie.description, "Une description de test")
        self.assertEqual(self.poesie.poeme, "<p>Contenu du poème de test</p>")
        self.assertTrue(self.poesie.status)  # Par défaut status est True
        
    def test_poesie_str_method(self):
        # Tester la méthode __str__
        self.assertEqual(str(self.poesie), "Test Poème")

    def test_verbose_name(self):
        # Tester les noms verbeux du modèle
        self.assertEqual(Poesie._meta.verbose_name, 'Poésie')
        self.assertEqual(Poesie._meta.verbose_name_plural, 'Poésies')

    def test_dates_auto_now(self):
        # Tester que les dates sont automatiquement définies
        self.assertIsNotNone(self.poesie.date_add)
        self.assertIsNotNone(self.poesie.date_update)

    def test_titre_max_length(self):
        # Tester la longueur maximale du titre
        titre_trop_long = "x" * 256  # Dépasse la limite de 255 caractères
        poesie = Poesie(
            titre=titre_trop_long,
            description="Test",
            poeme="<p>Test</p>"
        )
        try:
            poesie.full_clean()
        except ValidationError:
            pass  # Si une ValidationError est levée, le test passe
        else:
            self.fail("ValidationError was not raised for a title exceeding max length")

    def test_status_default(self):
        # Tester la valeur par défaut du status
        nouvelle_poesie = Poesie.objects.create(
            titre="Autre poème",
            description="Description",
            poeme="<p>Contenu</p>"
        )
        self.assertTrue(nouvelle_poesie.status)

    def test_update_date_modification(self):
        # Tester la mise à jour automatique de date_update
        date_initiale = self.poesie.date_update
        time.sleep(0.1)  # Attendre un peu pour s'assurer que la date change
        self.poesie.description = "Description modifiée"
        self.poesie.save()
        self.poesie.refresh_from_db()  # Recharger l'objet depuis la base de données
        self.assertNotEqual(self.poesie.date_update, date_initiale)

    def test_html_dans_poeme(self):
        # Tester que le champ poeme accepte le HTML
        html_content = "<p>Test</p><strong>Gras</strong><em>Italique</em>"
        self.poesie.poeme = html_content
        self.poesie.save()
        poesie_rechargee = Poesie.objects.get(pk=self.poesie.pk)
        self.assertEqual(poesie_rechargee.poeme, html_content)
