from django.db import models
from tinymce import HTMLField
# Create your models here.
class Poesie(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    poeme = HTMLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Poésie'
        verbose_name_plural = 'Poésies'

    def __str__(self):
            return self.titre

