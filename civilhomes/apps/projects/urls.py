from django.urls import path
from . import views

urlpatterns = [
    path('search', views.AllProjectsSearch.as_view(), name="projects_search"),
    path('detail/<int:id>', views.ProjectDetail.as_view(), name="project_detail")
]
