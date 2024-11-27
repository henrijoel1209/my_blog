from django.urls import path
from.import views

urlpatterns = [
        path('', views.timeline, name='timeline'),  
        path('detail/<slug>', views.detail, name='detail'),
        path('cours', views.cours, name='cours'),
        path('is_reponsescommentaires', views.is_reponsescommentaires, name='is_reponsescommentaires'),
        path('is_commentaire', views.is_commentaire, name='is_commentaire'),
        path('video', views.video, name='video'),
        path('evenement', views.evenement, name='evenement'),
        path('details/<slug>', views.details_events, name='details'),
        path('textes', views.textes, name='textes'),
] 