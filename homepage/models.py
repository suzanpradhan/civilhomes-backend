from django.db import models
from imagegallery import models as imagegallery_models
from projects import models as project_models



class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ForeignKey(imagegallery_models.Image, on_delete=models.CASCADE)

class VideoSection(models.Model):
    videoTitle = models.CharField(max_length=255)
    videoLink = models.CharField(max_length=255)

class Companies(models.Model):
    name = models.CharField(max_length=255)
    companyLogo = models.ForeignKey(imagegallery_models.Image, on_delete=models.CASCADE)

class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    contactEmail = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)

class HomePageBasic(models.Model):
    headerTitle = models.CharField(max_length=255)
    headerDescription = models.TextField()
    services = models.ManyToManyField(Service)
    videoSection = models.ForeignKey(VideoSection, on_delete=models.CASCADE)
    promotedProject = models.ForeignKey(project_models.Project, on_delete=models.CASCADE, related_name='promoted_projects')
    ongoingProjects = models.ManyToManyField(project_models.Project, related_name="ongoing_projects")
    companies = models.ManyToManyField(Companies)
    location = models.ForeignKey(project_models.Location, on_delete=models.CASCADE)
    contactInfo = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)


