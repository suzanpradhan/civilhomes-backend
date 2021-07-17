from django.db import models
from civilhomes.apps.imagegallery.models import Image

class ProjectPlan(models.Model):
    sheet_url = models.FileField(upload_to="project_sheet_files/")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    iframe_snippet = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Amenitie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Info(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProjectInfo(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

class Project(models.Model):
    status = (
        (1, "Not Started"),
        (2, "Ongoing"),
        (3, "Completed"),
        (4, "On Hold")
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    status = models.IntegerField(choices=status, default=1)
    brochure_url = models.FileField(upload_to="brochures/")
    project_plan = models.ForeignKey(ProjectPlan, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    amenities = models.ManyToManyField(Amenitie)
    project_images = models.ManyToManyField(Image)
    project_infos = models.ManyToManyField(ProjectInfo)

    def __str__(self):
        return self.name




class ProjectExtrasCard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
