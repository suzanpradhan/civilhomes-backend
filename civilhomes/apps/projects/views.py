from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ProjectSearchForm
from .models import Project, Amenitie, ProjectInfo
from django.db.models import Q
from civilhomes.apps.imagegallery import models as image_gallery_models



class AllProjectsSearch(TemplateView):
    template_name = "projects/index.html"
    form_class =  ProjectSearchForm

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        return render(request, self.template_name, {"projects":projects})

    def post(self, request, *args):
        title = request.POST.get("search_value")
        print(title)
        if (title is not "" or None):
            print("done")
            projects = Project.objects.filter(Q(name__contains=title))
        else:
            projects = Project.objects.all()
        print(projects)

        # return HttpResponse(title)
        return render(request, self.template_name, {"projects": projects, "title": title})


class ProjectDetail(TemplateView):
    template_name = "projects/project_detail.html"

    def get(self, request,id,  *args, **kwargs):
        status = (
        "Not Started",
        "Ongoing",
        "Completed",
        "On Hold"
        )
        project = Project.objects.get(id=id)
        projectGallery = image_gallery_models.ImageGallery.objects.filter(project=project)
        project.status = status[project.status-1]
        projectAmenitie = Amenitie.objects.filter(project=project)
        projectProjectInfo = ProjectInfo.objects.filter(project=project)
        context = {
            "project": project,
            "projectGallery": projectGallery,
            "projectAmenities": projectAmenitie,
            "projectProjectInfos":projectProjectInfo
        }
        return render(request, self.template_name, context)