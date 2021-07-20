from django.db import models

class Banner(models.Model):
    name=models.CharField(max_length=255,null=False)
    image = models.ImageField(upload_to = 'services/', null=True)

class Link(models.Model):
    name=models.CharField(max_length=255,null=False)
    url=models.CharField(max_length=255,null=True)
    active=models.BooleanField(default=False)
