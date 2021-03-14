from django.contrib import admin

from .models import ProjectPlan,Project,Location,Amenitie, Info, ProjectInfo, ProjectExtrasCard

admin.site.register(ProjectPlan)
admin.site.register(Project)
admin.site.register(Location)
admin.site.register(Amenitie)
admin.site.register(Info)
admin.site.register(ProjectInfo)
admin.site.register(ProjectExtrasCard)