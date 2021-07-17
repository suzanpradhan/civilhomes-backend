from civilhomes.apps.projects.models import Project
from django.shortcuts import render
from django.views.generic import TemplateView
from civilhomes.apps.imagegallery import models as imagegallery_models
from .models import Service, HomePageBasic
from civilhomes.apps.projects import models as projects_models
from civilhomes.apps.floorplan import models as floorplan_models
from django.core.serializers import json
from json import dumps

class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        mainHomeData = HomePageBasic.objects.first()
        if mainHomeData.videoSection.videoLink is not None:
            mainHomeData.videoSection.videoLink = mainHomeData.videoSection.videoLink.replace("watch?v=","embed/")
        service = Service.objects.all()
        promotedProject = mainHomeData.promotedProject
        promotedProjectInfos = projects_models.ProjectInfo.objects.filter(project=promotedProject)[:7]
        promotedProjectHouseTypes = floorplan_models.HouseType.objects.filter(project=promotedProject)
        promotedProjectImages = imagegallery_models.ImageGallery.objects.filter(project=promotedProject)
        projects_floorplans = {}
        for promotedProjectHouseType  in promotedProjectHouseTypes:
            projects_floorplans[promotedProjectHouseType] = floorplan_models.FloorPlan.objects.filter(project=promotedProject, house_type=promotedProjectHouseType)
        ongoingProjects = mainHomeData.ongoingProjects.all()
        ongoingProjectsLocation = json.Serializer().serialize([(projects_models.Location.objects.get(id=ongoingProject.location.id)) for ongoingProject in ongoingProjects])
        print(ongoingProjectsLocation)
        companies = mainHomeData.companies.all()
        testPhase = {
            "name":"uallal",
            "lat":85.31403,
            "long":27.6793064
        }
        contactInfo = mainHomeData.contactInfo

        context = {"services": service, 
                    "mainHomeData": mainHomeData, 
                    "promotedProject":promotedProject,
                    "companies": companies,
                    "testData": dumps(testPhase), 
                    "contactInfo":contactInfo,
                    "promotedProjectInfos":promotedProjectInfos, 
                    "projects_floorplans":projects_floorplans, 
                    "promotedProjectHouseTypes":promotedProjectHouseTypes,
                    "ongoingProjectsJson": json.Serializer().serialize(ongoingProjects),
                    "ongoingProjectsLocation": ongoingProjectsLocation,
                    "promotedProjectImages":promotedProjectImages}
        return render(request, self.template_name, context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        mainHomeData = HomePageBasic.objects.first()
        contactInfo = mainHomeData.contactInfo

        return render(request, self.template_name, {"contactInfo":contactInfo})

