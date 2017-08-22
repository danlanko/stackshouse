from django.shortcuts import render_to_response
from models import *

# Create your views here.

def homepage(request):
    slide_image =  Slider.objects.all()
    return render_to_response('index.html', {'slide_image': slide_image,})

def about(request):

    return render_to_response('about.html')

def showreel(request):
    showreel = ShowReel.objects.all()

    return render_to_response('show_reel.html')

def photogallery(request):

    return render_to_response('photo_gallery.html')

def contact (request):

    return render_to_response('contact.html')