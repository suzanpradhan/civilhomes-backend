from django.contrib import admin

from .models import ProjectPlan, Project, Location, Amenitie, Info, ProjectInfo, ProjectExtrasCard


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'address')


class ProjectInfoAdmin(admin.ModelAdmin):
    list_display = ('project', 'info', 'value')


class ProjectExtrasCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'project')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')


class AmenitieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project')


admin.site.register(ProjectPlan)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Amenitie, AmenitieAdmin)
admin.site.register(Info)
admin.site.register(ProjectInfo, ProjectInfoAdmin)
admin.site.register(ProjectExtrasCard, ProjectExtrasCardAdmin)
