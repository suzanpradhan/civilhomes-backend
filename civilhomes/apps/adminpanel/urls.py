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
    path('service/<int:id>/delete', views.DeleteServices.as_view(), name="admin-service-delete"),
    path('blog/add', views.Blogs.as_view(), name="admin-blog-add"),
    path('blog/all', views.ListBlogs.as_view(), name="admin-blog-all"),
    path('blog/<int:id>/update', views.UpdateBlog.as_view(), name="admin-blog-update"),
    path('blog/<int:id>/delete', views.DeleteBlogs.as_view(), name="admin-blog-delete"),
    path('banner/add', views.Banners.as_view(), name="admin-banner-add"),
    path('banner/all', views.ListBanner.as_view(), name="admin-banner-all"),
    path('banner/<int:id>/update', views.UpdateBanner.as_view(), name="admin-banner-update"),
    path('banner/<int:id>/delete', views.DeleteBanner.as_view(), name="admin-banner-delete"),
    path('link/add', views.Links.as_view(), name="admin-link-add"),
    path('link/all', views.ListLink.as_view(), name="admin-link-all"),
    path('link/<int:id>/update', views.UpdateLink.as_view(), name="admin-link-update"),
    path('link/<int:id>/delete', views.DeleteLink.as_view(), name="admin-link-delete"),
    path('company/add', views.AddCompany.as_view(), name="admin-company-add"),
    path('company/all', views.ListCompany.as_view(), name="admin-company-all"),
    path('company/<int:id>/update', views.UpdateCompany.as_view(), name="admin-company-update"),
    path('company/<int:id>/delete', views.DeleteCompany.as_view(), name="admin-company-delete"),

]
