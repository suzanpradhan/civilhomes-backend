from django.contrib import admin

from .models import Floor, FloorPlan, HouseType


class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')

class FloorPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor', 'dimension', 'project')

admin.site.register(Floor)
admin.site.register(FloorPlan, FloorPlanAdmin)
admin.site.register(HouseType, HouseTypeAdmin)
