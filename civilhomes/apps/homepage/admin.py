from django.contrib import admin

from .models import Service, HomePageBasic, VideoSection, Companies, ContactInfo

admin.site.register(HomePageBasic)
admin.site.register(Service)
admin.site.register(VideoSection)
admin.site.register(Companies)
admin.site.register(ContactInfo)
