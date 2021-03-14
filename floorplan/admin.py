from django.contrib import admin

from .models import Floor, FloorPlan, HouseType

admin.site.register(Floor)
admin.site.register(FloorPlan)
admin.site.register(HouseType)
