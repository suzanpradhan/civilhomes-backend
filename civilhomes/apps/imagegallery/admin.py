from django.contrib import admin

from .models import Image
from .models import ImageGallery


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'image_type')


class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'gallery_type', 'project')


admin.site.register(Image, ImageAdmin)
admin.site.register(ImageGallery, ImageGalleryAdmin)
