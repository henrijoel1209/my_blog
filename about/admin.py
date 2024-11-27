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

class CurriculumAdmin(CustomAddmin):
    list_display = ('nom','cv','date_add','date_update','status','photo_view')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [ 
                  ("info curriculum",{"fields":["nom","cv","description","photo"]}),
                  ("standard",{"fields":["status"]})
    ]
    def photo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.photo.url))

class ContactAdmin(CustomAddmin):
    list_display = ('nom','email','subject','date_add','date_update','status')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info contact",{"fields":["nom","email","subject","message","telephone"]}),
                  ("standard",{"fields":["status"]})
    ]

class PrestationAdmin(CustomAddmin):
    list_display = ('titre','date_add','date_update','status','image_view')   
    search_fields = ('titre',)    
    ordering = ['titre']    
    fieldsets = [
                  ("info prestation",{"fields":["titre","description","image"]}),
                  ("standard",{"fields":["status"]})
    ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class GallerieAdmin(CustomAddmin):
    list_display = ('titre','date_add','date_update','status','gallerie_views')   
    search_fields = ('titre',)    
    ordering = ['titre']    
    fieldsets = [
                  ("info prestation",{"fields":["gallerie","titre"]}),
                  ("standard",{"fields":["status"]})
    ]
    def gallerie_views(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.gallerie.url))

class PresentationAdmin(CustomAddmin):
    list_display = ('titre','date_add','date_update','status','image_view')   
    search_fields = ('titre',)    
    ordering = ['titre']    
    fieldsets = [
                  ("info présentation",{"fields":["titre","description","image"]}),
                  ("standard",{"fields":["status"]})
    ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Curriculum,CurriculumAdmin)
_register(models.Contact,ContactAdmin)
_register(models.Prestation,PrestationAdmin)
_register(models.Presentation,PresentationAdmin)
_register(models.Gallerie,GallerieAdmin)