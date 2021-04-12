from django import forms
from .models import Project

class ProjectSearchForm(forms.Form):
    title = forms.CharField()
    property_type = forms.CharField()
    location = forms.CharField()
    area = forms.CharField()

    def filter_projects(self):
        allprojects = Project.objects.all()
        if (self.title is not "" or None):
            self.projects = Project.objects.filter(name=self.title)
        return self.projects
