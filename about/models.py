from django.db import models
from tinymce import HTMLField
from website.models import SiteInfo
# Create your models here.

class Curriculum(models.Model):
    photo = models.ImageField(upload_to='images/curriculum')
    nom = models.CharField(max_length=255)
    description = HTMLField()
    cv = models.FileField(upload_to='cv/curriculim')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Curriculum'
        verbose_name_plural = 'Curriculum'

    def __str__(self):
            return self.nom

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    subject =models.CharField(max_length=255)
    telephone = models.IntegerField(null=True)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
            return self.nom

class Prestation(models.Model): 
    titre = models.CharField(max_length=255)
    description = models.TextField() 
    image = models.ImageField(upload_to='images/prestations')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Prestation'
        verbose_name_plural = 'Prestations'

    def __str__(self):
            return self.titre

class Presentation(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/presentation')
    description =HTMLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
            return self.titre

class Gallerie(models.Model):
    gallerie = models.ImageField(upload_to='gallerie/image',null=True)
    titre = models.CharField(max_length=255,null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Gallerie'
        verbose_name_plural = 'Galleries'

    def __str__(self):
            return self.titre



