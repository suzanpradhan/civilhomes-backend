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
    path('project/<int:id>/delete', views.DeleteProject.as_view(), name="admin-project-delete"),
    path('service/add', views.Services.as_view(), name="admin-service-add"),
    path('service/all', views.ListServices.as_view(), name="admin-service-all"),
    path('service/<int:id>/update', views.UpdateServices.as_view(), name="admin-service-update"),
    path('service/<int:id>/delete', views.DeleteProject.as_view(), name="admin-service-delete"),
    path('blog/add', views.Blogs.as_view(), name="admin-blog-add"),
    path('blog/all', views.ListBlogs.as_view(), name="admin-blog-all"),
    path('blog/<int:id>/update', views.UpdateBlog.as_view(), name="admin-blog-update"),
    path('blog/<int:id>/delete', views.DeleteBlogs.as_view(), name="admin-blog-delete"),
]
