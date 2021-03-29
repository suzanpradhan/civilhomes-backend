from django.shortcuts import render
from django.views.generic import TemplateView
from civilhomes.apps.imagegallery import models as imagegallery_models
from .models import Service, HomePageBasic

class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        mainHomeData = HomePageBasic.objects.first()
        if mainHomeData.videoSection.videoLink is not None:
            mainHomeData.videoSection.videoLink = mainHomeData.videoSection.videoLink.replace("watch?v=","embed/")
        service = Service.objects.all()
        print(service)
        return render(request, self.template_name, {"services": service, "mainHomeData": mainHomeData})