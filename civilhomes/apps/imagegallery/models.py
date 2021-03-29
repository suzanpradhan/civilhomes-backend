from django.db import models
from civilhomes.apps.projects import models as projects_model


class Image(models.Model):
    image_name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200)
    image_type = models.CharField(max_length=10)

    def __str__(self):
        return self.image_name


class ImageGallery(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    gallery_type = models.CharField(max_length=100)
    project = models.ForeignKey(projects_model.Project, on_delete=models.CASCADE)
