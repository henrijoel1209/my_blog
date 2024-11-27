from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
        path('', views.about, name='about'),
        path('contact', views.contact, name='contact'),        
        path('author', views.author, name='author'),  
        path('is_contact', views.is_contact, name='is_contact'),  
]