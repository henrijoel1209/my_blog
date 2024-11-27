from django.db import models

# Create your models here.
 
class SiteInfo(models.Model):
    email = models.EmailField()
    nom = models.CharField(max_length=255)
    telephone = models.IntegerField()
    description = models.TextField()
    logo = models.ImageField(upload_to='logo/site')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Site info'
        verbose_name_plural = 'Sites infos'

    def __str__(self):
        return self.nom 

class SocialCount(models.Model):
    ICONES = [
        ('facebook','fa-facebook-f'),
        ('twitter','fa-twitte'),
    ]
    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icones = models.CharField(choices=ICONES,max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "réseau social"
        verbose_name_plural = "réseaux sociaux"

    def __str__(self):
        return self.reseau

class Newsletter(models.Model):
    email = models.EmailField(null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

    def __str__(self):
        return self.email