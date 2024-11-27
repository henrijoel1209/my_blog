from django.db import models
from tinymce import HTMLField
from django.utils.text import slugify
from datetime import datetime
from django.core.exceptions import ValidationError
from website.models import SiteInfo

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
            return self.nom

class Publication(models.Model):
    titre = models.CharField(max_length=255)
    description = HTMLField()
    image = models.ImageField(upload_to='image/publication')
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='categorie_publication')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug = '-'.join((slugify(self.titre),slugify(datetime.now().microsecond)))
        super(Publication,self).save(*args, **kwargs)
    
 
    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'

    def __str__(self):
            return self.titre

class Commentaire(models.Model):
    publication = models.ForeignKey(Publication,on_delete=models.CASCADE,related_name='publication_commentaire')
    nom = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    commentaire = models.TextField(null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
            return self.nom

class ReponseCommentaire(models.Model):
    commentaire = models.ForeignKey(Commentaire,on_delete=models.CASCADE,related_name='reponse_commentaire',null=True)
    nom = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    reponse = models.TextField(null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Reponse Commentaire'
        verbose_name_plural = 'Reponses Commentaires'

        def __str__(self):
            return self.nom

class Like(models.Model):
    publication = models.ForeignKey(Publication,on_delete=models.CASCADE,related_name='like_publication')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'

    def __str__(self):
            return self.publication.titre

class Evenement(models.Model):
    image = models.ImageField(upload_to='evenemant/image')
    description = HTMLField()
    titre = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug = '-'.join((slugify(self.titre),slugify(datetime.now().microsecond)))
        super(Evenement,self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Evenement'
        verbose_name_plural = 'Evenements'

    def __str__(self):
            return self.titre

class Cours(models.Model):
    titre = models.CharField(max_length=255)
    niveau = models.CharField(max_length=255)
    annee = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="cours/image", default="cours/pdf.png")
    cours = models.FileField(upload_to='cours/cours')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'

    def clean(self):
        if self.annee is not None and self.annee < 0:
            raise ValidationError({'annee': 'L\'année ne peut pas être négative.'})

    def __str__(self):
            return self.titre

class Textes(models.Model):
    titre = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="textes/image", default="cours/pdf.png")
    pdf = models.FileField(upload_to="pdf/textes",null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Texte de référence'
        verbose_name_plural = 'Textes de références '

    def __str__(self):
            return self.titre

class Video(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="video/image", default="video/video.png")
    video = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Vidéo'
        verbose_name_plural = 'Vidéos'

    def __str__(self):
            return self.titre


    @property
    def get_video(self):
        try:
            data = self.video.rsplit("=")
            return data[1]
        except:
            pass 
