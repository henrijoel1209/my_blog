from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
        path('contact/submit/', views.contact_submit, name='contact_submit'),
        path('is_newsletter', views.is_newsletter, name='is_newsletter'),
]