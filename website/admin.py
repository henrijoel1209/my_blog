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

class SiteInfoAdmin(CustomAddmin):
    list_display = ('email','nom','telephone','date_add','date_update','status','logo_view')   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info sites info",{"fields":["email","logo","nom","telephone","description"]}),
                  ("standard",{"fields":["status"]})
    ]
    def logo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo.url))
 
class NewsletterAdmin(CustomAddmin):
    list_display = ('email','date_add','date_update','status')   
    search_fields = ('email',)    
    ordering = ['email']    
    fieldsets = [
                  ("info newsletter",{"fields":["email"]}),
                  ("standard",{"fields":["status"]})
    ]

class SocialCountAdmin(CustomAddmin):
    list_display = ('nom','lien','date_add','date_update','status',)   
    search_fields = ('nom',)    
    ordering = ['nom']    
    fieldsets = [
                  ("info réseaux sociaux",{"fields":["nom","lien","icones"]}),
                  ("standard",{"fields":["status"]})
    ]

def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.SiteInfo,SiteInfoAdmin)
_register(models.SocialCount,SocialCountAdmin)
_register(models.Newsletter,NewsletterAdmin)
