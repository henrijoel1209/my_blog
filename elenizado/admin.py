from django.contrib import admin
from.import models
from django.utils.safestring import mark_safe

# Register your models here.
class CustomAddmin(admin.ModelAdmin):
    actions = ('activate','desactivate')
    list_filter = ('status',)
    list_per_page = 20
    date_hierachy = "date_add"

    def activate(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selection a été effectué avec succes')
    activate.short_description = "permet d'activer le champs selectionner"

    def desactivate(self,request,queryset):  
        queryset.update(status=False)
        self.message_user(request,'la selection a été effectué avec succes')
    desactivate.short_description = "permet de desactiver le champs selectionner"

class CategorieAdmin(CustomAddmin):
    list_display = ('nom','date_add','date_update','status')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info catégorie",{"fields":["nom","description"]}),
                  ("standard",{"fields":["status"]})
    ]

class PublicationAdmin(CustomAddmin):
    list_display = ('titre','categorie','date_add','date_update','status','image_view')   
    search_fields = ('titre',)    
    ordering = ['titre']    
    fieldsets = [
                  ("info publication",{"fields":["image","titre","description","categorie"]}),
                  ("standard",{"fields":["status"]})
    ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


class CommentaireAdmin(CustomAddmin):
    list_display = ('nom','date_add','date_update','status')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info commentaire",{"fields":["nom","commentaire","commentaires","publication"]}),
                  ("standard",{"fields":["status"]})
    ]
    

class LikeAdmin(CustomAddmin):
    list_display = ('publication','date_add','date_update','status')   
    search_fields = ('publication',)    
    ordering = ['publication']    
    fieldsets = [
                  ("info like",{"fields":["publication",]}),
                  ("standard",{"fields":["status"]})
    ]
 
class ReponseCommentaireAdmin(CustomAddmin):
    list_display = ('nom', 'commentaire','date_add','date_update','status')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info reponse commentaire",{"fields":["reponse","nom","commentaire","email"]}),
                  ("standard",{"fields":["status"]})
    ]

class EvenementAdmin(CustomAddmin):
    list_display = ('titre','date_add','date_update','status','image_view')   
    search_fields = ('titre',)    
    ordering = ['titre']    
    fieldsets = [
                  ("info événement",{"fields":["titre","description","image"]}),
                  ("standard",{"fields":["status"]})
    ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


class CoursAdmin(CustomAddmin):
    list_display = ('titre','niveau','annee','date_add','date_update','status','cours')   
    search_fields = ('titre',)    
    ordering = ['titre']    
    fieldsets = [
                  ("info cours",{"fields":["titre","niveau","annee","cours","description"]}),
                  ("standard",{"fields":["status"]})
    ]
class TextesAdmin(CustomAddmin):
    list_display = ('titre','date_add','date_update','status','pdf')   
    search_fields = ('titre',)    
    ordering = ['titre']    
    fieldsets = [
                  ("info cours",{"fields":["titre","description","pdf"]}),
                  ("standard",{"fields":["status"]})
    ]


class VideoAdmin(CustomAddmin):
    list_display = ('titre','date_add','date_update','status','video')   
    search_fields = ('titre',)    
    ordering = ['titre']    
    fieldsets = [
                  ("info vidéo",{"fields":["video","titre","description"]}),
                  ("standard",{"fields":["status"]})
    ]
    
    
def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Categorie,CategorieAdmin)
_register(models.Publication,PublicationAdmin)
_register(models.Commentaire,CommentaireAdmin)
_register(models.ReponseCommentaire,ReponseCommentaireAdmin)
_register(models.Like,LikeAdmin)
_register(models.Evenement,EvenementAdmin)
_register(models.Cours,CoursAdmin)
_register(models.Video,VideoAdmin)
_register(models.Textes,TextesAdmin)
