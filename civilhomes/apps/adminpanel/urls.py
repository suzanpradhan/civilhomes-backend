from django.urls import path
from . import views
from . import apis

# URLS OF ADMIN
urlpatterns = [
    path('dashboard', views.Dashboard.as_view(), name="admin-dashboard"),
    path('login', views.AdminLogin.as_view(), name="admin-login"),
    path('logout/', views.logoutAdminLogOut, name='admin-logout')
]

# HOMEPAGE URLS
urlpatterns += [
    path('homepage/edit', views.HomePageGeneralSettings.as_view(), name="admin-homepage-general-settings")
]

# PROJECT URLS
urlpatterns += [
    path('project/add', views.AddProject.as_view(), name="admin-project-add"),
    path('project/amenities/add', views.AddAmenitie.as_view(), name="admin-amenitie-add"),
    path('project/image/add', views.AddImage.as_view(), name="admin-image-add"),
    path('project/all', views.ListProject.as_view(), name="admin-project-all"),
    path('project/<int:id>/update', views.UpdateProject.as_view(), name="admin-project-update"),
    path('project/<int:id>/delete', views.DeleteProject.as_view(), name="admin-project-delete")
]

