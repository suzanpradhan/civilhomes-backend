from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.Dashboard.as_view(), name="admin-dashboard"),
]

urlpatterns += [
    path('homepage/edit', views.HomePageGeneralSettings.as_view(), name="admin-homepage-general-settings")
]

