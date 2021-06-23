from django.shortcuts import render
from .models import Gallery, Volunteer, Programme, Blog

def gallery(request):
    gallery_obj = Gallery.objects.all()
    context = {
        'obj' : gallery_obj,
    }

    return render(request,"index.html",context)

def volunteer(request):
    volunteer_obj = Volunteer.objects.all()
    context = {
        'obj' : volunteer_obj,
    }

    return render(request,"index.html",context)

def programme(request):
    programme_obj = Programme.objects.all()
    context = {
        'obj' : programme_obj,
    }

    return render(request,"index.html",context)

def blog(request):
    blog_obj = Blog.objects.all()
    context = {
        'obj' : blog_obj,
    }

    return render(request,"index.html",context)

