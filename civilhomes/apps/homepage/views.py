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
        promotedProject = mainHomeData.promotedProject
        companies = mainHomeData.companies.all()
        testPhase = {
            "name":"uallal",
            "lat":85.31403,
            "long":27.6793064
        }
        contactInfo = mainHomeData.contactInfo
        return render(request, self.template_name, {"services": service, "mainHomeData": mainHomeData, "promotedProject":promotedProject, "companies": companies,
        "testData": dumps(testPhase), "contactInfo":contactInfo})