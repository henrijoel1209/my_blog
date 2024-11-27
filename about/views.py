from django.shortcuts import render
from . import models
from website import models as models_site
from . import views
import json
from django.http import JsonResponse 
from django.core.validators import validate_email

# Create your views here.
def about(request):
    site_info = models_site.SiteInfo.objects.filter(status=True)[:1].get()
    about = models.Presentation.objects.filter(status=True)[:1]
    datas = {
            "about": about,
            "site_info": site_info,
    }
    return render(request, 'pages/about-us.html', datas)

def contact(request):
    site_info = models_site.SiteInfo.objects.filter(status=True)[:1].get()
    datas = {
            'site_info': site_info,
    }
    return render(request, 'pages/contact.html', datas)

def author(request):
    site_info = models_site.SiteInfo.objects.filter(status=True)[:1].get()
    curriculum = models.Curriculum.objects.filter(status=True)[:1].get() 
    datas = {
            "curriculum": curriculum,
            "site_info": site_info,
    }
    return render(request, 'pages/author-posts-2.html', datas)

def is_contact(request):
        message = "" 
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        tel = request.POST.get('tel')
        message = request.POST.get('messages')
        try:
            validate_email(email)
            isemail = True
            if isemail and not email.isspace() and email is not None and name is not None and message is not None:
                success = False
                print("1")
                contact = models.Contact(
                    nom = name,
                    email = email,
                    telephone = tel,
                    subject = subject,
                    message = message
                )
                contact.save()
                print("3")
                success = True
                message = "l'enregistrement a bien été effectué"
        except :
            message = "email incorrect"
            print("2")
          
        data =   {
        "success":success,
        "message":message,

     }
        return JsonResponse(data,safe=False)