from django.db import models
from projects import models as project_models
from imagegallery import models as imagegallery_models


class HouseType(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(project_models.Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Floor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FloorPlan(models.Model):
    dimension = (
        (1, "2D"),
        (2, "3D")
    )
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    project = models.ForeignKey(project_models.Project, on_delete=models.CASCADE)
    image = models.ForeignKey(imagegallery_models.Image, on_delete=models.CASCADE)
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    dimension = models.IntegerField(choices=dimension, default=1)

    def __str__(self):
        return self.name
