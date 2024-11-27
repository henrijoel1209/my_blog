from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models 
from elenizado import models as elenizado_models
from about import models as about_models
import json
from django.http import JsonResponse 
from django.core.validators import validate_email

# Create your views here.
def index(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    publication_r = elenizado_models.Publication.objects.all().order_by('-date_add')[:4]
    events_r = elenizado_models.Evenement.objects.all().order_by('-date_add')[:3]
    gallerie = about_models.Gallerie.objects.filter(status=True)
    publication_list = elenizado_models.Publication.objects.all().order_by('-date_add')
    page = request.GET.get('page', 1)
    paginator = Paginator(publication_list, 4)
    try:
        pub = paginator.page(page)
    except PageNotAnInteger:
        pub = paginator.page(1)
    except EmptyPage:
        pub = paginator.page(paginator.num_pages)
    datas = {
             'publication_r':publication_r,
             'events_r':events_r,
             'gallerie':gallerie,
             'site_info':site_info,
             'pub':pub,
    }
    return render(request,'pages/index.html',datas)

def about(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    return render(request, 'pages/about.html', {'site_info': site_info})

def contact(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    return render(request, 'pages/contact.html', {'site_info': site_info})

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('nname')
        email = request.POST.get('eemail')
        tel = request.POST.get('wwebsite')
        subject = request.POST.get('ssubject')
        message = request.POST.get('mmessage')
        
        try:
            contact = models.Contact(
                name=name,
                email=email,
                telephone=tel,
                subject=subject,
                message=message
            )
            contact.save()
            return JsonResponse({
                'success': True,
                'message': 'Your message has been sent successfully!'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'An error occurred. Please try again.'
            })
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    })

def is_newsletter(request):
    message = "" 
    success = False  # Initialisation de success par défaut
    email = request.POST.get('email')
    try:
        validate_email(email)
        newsletter = models.Newsletter(
            email = email,
        )
        newsletter.save()
        success = True
        message = "l'enregistrement a bien été effectué"
    except :
        message = "email incorrect"
    data =   {
    "success":success,
    "message":message,

    }
    return JsonResponse(data)
