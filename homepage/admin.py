from django.contrib import admin

from .models import Service, HomePageBasic, VideoSection

admin.site.register(HomePageBasic)
admin.site.register(Service)
admin.site.register(VideoSection)