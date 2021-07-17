from django.db import models
# from civilhomes.apps.projects import models as projects_model


class Image(models.Model):
    types = (
        (1, "2D"),
        (2, "3D")
    )
    image_types = (
        (1, "Ongoing"),
        (2, "Completed")
    )
    image_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'services/', null=True)
    image_type = models.IntegerField(choices=image_types, default=2)
    dimension = models.IntegerField(choices=types, default=1)

    def __str__(self):
        return self.image_name


# class ImageGallery(models.Model):
#     image = models.ForeignKey(Image, on_delete=models.CASCADE)
#     gallery_type = models.CharField(max_length=100)
#     project = models.ForeignKey(projects_model.Project, on_delete=models.CASCADE)
# border: 5px solid #fff;
#     width: 100%;
#     box-shadow: 1px 3px 8px #bfbfbf;