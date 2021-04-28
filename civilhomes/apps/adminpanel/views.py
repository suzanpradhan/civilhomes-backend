from django.shortcuts import render
from django.views.generic import TemplateView

class Dashboard(TemplateView):
    template_name = 'adminpanel/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class HomePageGeneralSettings(TemplateView):
    template_name = "adminpanel/homepage/general_settings.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)