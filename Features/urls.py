from django.urls import path
from django.urls.conf import include
from . import views 
from django.views.generic.base import RedirectView

urlpatterns = [
    path('gallery/',views.gallery,name='gallery'),
    path('volunteer/',views.volunteer,name='volunteer'),
    path('programme/',views.gallery,name='programme'),
    path('blog/',views.gallery,name='blog'),
]
