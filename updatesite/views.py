from django.shortcuts import render_to_response
from models import *
from blog.models import BlogPost

# Create your views here.

def homepage(request):
    slide_image =  Slider.objects.all()
    blog = list(BlogPost.objects.all())
    index_blog = blog[:-4:-1]

    return render_to_response('index.html', {'slide_image': slide_image,'index_blog':index_blog})

def about(request):

    return render_to_response('about.html')

def showreel(request):
    showreel = ShowReel.objects.all()
    video_catgory = SetVideoCategory.objects.all()
    return render_to_response('show_reel.html',{'showreel':showreel,'category':video_catgory})

def photogallery(request):
    picture = PhotoGallery.objects.all()
    photo_category = SetPhotoCategory.objects.all()
    return render_to_response('photo_gallery.html',{'picture':picture, 'photo_category':photo_category})

def contact (request):

    return render_to_response('contact.html')