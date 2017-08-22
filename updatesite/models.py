from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Slider(models.Model):
    slider_title = models.CharField(max_length=50)
    slider_image = models.ImageField(upload_to='slider_image')
    slider_desc = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Slider.objects.get(id=self.id)
            if this.slider_image != self.slider_image:
                this.slider_image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Slider, self).save(*args, **kwargs)

    def __str__(self):
        return (self.slider_title)

class SetPhotoCategory(models.Model):
    photo_gallery_category = models.CharField(max_length=100)

    def __str__(self):
        return (self.photo_gallery_category)

class SetVideoCategory(models.Model):
    video_category = models.CharField(max_length=100)

    def __str__(self):
        return (self.video_category)

class PhotoGallery(models.Model):
    select_category = models.ForeignKey(SetPhotoCategory)
    photo_title = models.CharField(max_length=50)
    upload_image = models.ImageField(upload_to='photo_gallery')

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = PhotoGallery.objects.get(id=self.id)
            if this.upload_image != self.upload_image:
                this.upload_image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(PhotoGallery, self).save(*args, **kwargs)
    def __str__(self):
        return (self.photo_title)

class ShowReel(models.Model):
    select_category = models.ForeignKey(SetVideoCategory)
    video_title = models.CharField(max_length=250, unique=True)
    video_id = models.CharField(max_length=250, help_text="Please copy and paste VIDEO ID only(eg: DhbtCIQuGv4)")

    def __str__(self):
        return (self.video_title)


