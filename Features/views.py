from django.shortcuts import render,get_object_or_404
from .models import Gallery, Volunteer, Programme, Blog

def home(request):
    blog_obj = Blog.objects.order_by("Date")[:3]
    programme_obj = Programme.objects.filter(Type="Campaign").order_by("Date")[:4]
    fundraiser_obj = Programme.objects.filter(Type="Fundraiser").order_by("Date")[:4]
    gallery_obj = Gallery.objects.all()


    context = {
        "blog_obj" : blog_obj,
        "programme_obj" : programme_obj,
        "fundraiser_obj" : fundraiser_obj,
        "gallery_obj" :gallery_obj,
    }

    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def gallery(request):
    gallery_obj = Gallery.objects.all()
    context = {
        'obj' : gallery_obj,
    }

    return render(request,"gallery.html",context)

def volunteer(request):
    volunteer_obj = Volunteer.objects.all()
    context = {
        'obj' : volunteer_obj,
    }

    return render(request,"volunteers.html",context)

def join_volunteer(request):
    pass



def campaign(request):
    programme_obj = Programme.objects.all()
    context = {
        'obj' : programme_obj,
    }

    return render(request,"campaign.html",context)

def fundraiser(request):
    programme_obj = Programme.objects.all()
    context = {
        'obj' : programme_obj,
    }

    return render(request,"fundraiser.html",context)

def programme_campaign(request,*args, **kwargs):
    programme_obj = get_object_or_404(Programme,pk=kwargs.get("pk"))
    context = {
        'obj' : programme_obj,
    }

    return render(request,"programme_campaign.html",context)

def programme_fundraiser(request,*args, **kwargs):
    programme_obj = get_object_or_404(Programme,pk=kwargs.get("pk"))
    context = {
        'obj' : programme_obj,
    }

    return render(request,"programme_fundraiser.html",context)


def blog(request):
    blog_obj = Blog.objects.all()
    context = {
        'obj' : blog_obj,
    }

    return render(request,"blog.html",context)

def blog_detail(request,*args, **kwargs):
    blog_obj = get_object_or_404(Blog,pk=kwargs.get("pk"))
    context = {
        'obj' : blog_obj,
    }

    return render(request,"blog_detail.html",context)