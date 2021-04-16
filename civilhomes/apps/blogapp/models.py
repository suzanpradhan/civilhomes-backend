from django.db import models
from ..imagegallery import models as image_gallery_models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    cover_images = models.ForeignKey(image_gallery_models.Image, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
