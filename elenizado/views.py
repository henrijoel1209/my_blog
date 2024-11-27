from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from.import models 
from about import models as about_models
from django.utils.text import slugify
from datetime import datetime
import json
from django.http import JsonResponse 
from django.core.validators import validate_email

def timeline(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    gallerie = about_models.Gallerie.objects.filter(status=True)
    events_r = models.Evenement.objects.all().order_by('-date_add')[:3] 
    publication = models.Publication.objects.filter(status=True).all()
    page = request.GET.get('page', 1)
    paginator = Paginator(publication, 4)
    try:
        pub = paginator.page(page)
    except PageNotAnInteger:
        pub = paginator.page(1)
    except EmptyPage:
        pub = paginator.page(paginator.num_pages)
    datas = {
            "publication":publication,
            "gallerie":gallerie,
            "events_r":events_r,
            'pub':pub,
    }
    return render(request,"pages/list-two-column.html",datas)

def detail(request,slug):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    publication_r = models.Publication.objects.all().order_by('-date_add')[:3]
    publication = models.Publication.objects.get(slug=slug)
    gallerie = about_models.Gallerie.objects.filter(status=True)
    events_r = models.Evenement.objects.all().order_by('-date_add')[:3]
    datas = {
            "publication":publication,
            "publication_r":publication_r,
            "events_r":events_r,
            "gallerie":gallerie,
            'site_info':site_info,
    }
    return render(request,"pages/detail-standart.html",datas)

def cours(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    events_r = models.Evenement.objects.all().order_by('-date_add')[:3]
    gallerie = about_models.Gallerie.objects.filter(status=True)
    cours = models.Cours.objects.filter(status=True).all()
    page = request.GET.get('page', 1)
    paginator = Paginator(cours, 4)
    try:
        cour = paginator.page(page)
    except PageNotAnInteger:
        cour = paginator.page(1)
    except EmptyPage:
        cour = paginator.page(paginator.num_pages)
    datas = {
            "cours":cours,
            "events_r":events_r,
            "gallerie":gallerie,
            "cour":cour,
    }
    return render(request,"pages/cours.html",datas)

def video(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    video = models.Video.objects.filter(status=True)
    datas = {
            "video":video,
    }
    return render(request,"pages/video-custom-player.html",datas)

def evenement(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    evenement = models.Evenement.objects.filter(status=True).all()
    events_r = models.Evenement.objects.all().order_by('-date_add')[:3]
    gallerie = about_models.Gallerie.objects.filter(status=True)
    publication = models.Publication.objects.filter(status=True).all()
    page = request.GET.get('page', 1)
    paginator = Paginator(evenement, 4)
    try:
        even = paginator.page(page)
    except PageNotAnInteger:
        even = paginator.page(1)
    except EmptyPage:
        even = paginator.page(paginator.num_pages)
    datas = {
                "evenement":evenement,
                "events_r":events_r,
                "gallerie":gallerie,
                'even':even,
                'site_info':site_info,
    }
    return render(request,"pages/evenements.html",datas)

def details_events(request,slug):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    events = models.Evenement.objects.get(slug=slug)
    events_r = models.Evenement.objects.all().order_by('-date_add')[:3]
    datas = {
            "events":events,
            "events_r":events_r,
            'site_info':site_info,

    }
    return render(request,"pages/details-events.html",datas)

def textes(request):
    site_info = models.SiteInfo.objects.filter(status=True)[:1].get()
    gallerie = about_models.Gallerie.objects.filter(status=True)
    events_r = models.Evenement.objects.all().order_by('-date_add')[:3]
    texte = models.Textes.objects.filter(status=True).all()
    page = request.GET.get('page', 1)
    paginator = Paginator(texte, 4)
    try:
        tex = paginator.page(page)
    except PageNotAnInteger:
        tex = paginator.page(1)
    except EmptyPage:
        tex = paginator.page(paginator.num_pages)
    datas = {
            "gallerie":gallerie,
            "events_r":events_r,
            "texte":texte,
            "tex":tex,
            'site_info':site_info,
    }
    return render(request,"pages/textes.html",datas)

def is_commentaire(request):
    message = "" 
    id = request.POST.get("id")
    print(id)
    nom = request.POST.get('nom')
    email = request.POST.get('email')
    commentaire = request.POST.get('commentaire')
    try:
        pub = models.Publication.objects.get(id=int(id))
    except :
        pub = ""
    try:
        validate_email(email)
        if email is not None and nom is not None and commentaire is not None:
            print("1")
            commentaire = models.Commentaire(
                nom = nom,
                email = email,
                commentaire = commentaire,
                publication = pub,
            )
            commentaire.save()
            print("3")
            success = True
            message = "l'enregistrement a bien été effectué"
    except Exception as e:
        print(e)
        success = False
        message = "email incorrect"
        print("2")
    try:
        
        all_comments = models.Commentaire.objects.filter(publication = pub)
        all_comment = [{'id':i.id, 'nom': i.nom, 'date' : i.date_add, 'commentaire': i.commentaire, 'reponse': [{'id':r.id, 'nom': r.nom, 'date' : r.date_add, 'reponse': r.reponse} for r in i.reponse_commentaire.all()]} for i in all_comments]
    except :
        all_comment = []
    datas= {
            "success":success,
            "message":message,
            'all_comment':all_comment,

    }
    return JsonResponse(datas,safe=False)

def is_reponsescommentaires(request):
    message = "" 
    id_commentaire = request.POST.get("id_commentaire")
    id = request.POST.get("id")
    print(id_commentaire)
    name = request.POST.get('name')
    mail = request.POST.get('mail')
    reponsecommentaires = request.POST.get('reponsecommentaires')
    try:
        com = models.Commentaire.objects.get(id=int(id_commentaire))
    except :
        com = ""
    try:
        validate_email(mail)
        if mail is not None and name is not None and reponsecommentaires is not None:
            print("1")
            reponses = models.ReponseCommentaire(
                nom = name,
                email = mail,
                reponse = reponsecommentaires,
                commentaire = com,
            )
            reponses.save()
            print("3")
            success = True
            message = "l'enregistrement a bien été effectué"
    except Exception as e:
        print(e)
        success = False
        message = "email incorrect"
        print("2")
    try:
        
        all_comments = models.Commentaire.objects.filter(publication__id= int(id))
        all_comment = [{'id':i.id, 'nom': i.nom, 'date' : i.date_add, 'commentaire': i.commentaire, 'reponse': [{'id':r.id, 'nom': r.nom, 'date' : r.date_add, 'reponse': r.reponse} for r in i.reponse_commentaire.all()]} for i in all_comments]
    except Exception as e:
        print(e)
        all_comment = []
    datas ={
            "success":success,
            "message":message,
            'all_comment':all_comment,
    }
    return JsonResponse(datas,safe=False)