from rest_framework import serializers
from civilhomes.apps.imagegallery import models as imageGallery_models

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = imageGallery_models.Image
        fields = ('id','image_name','image_url', 'image_type', 'dimension')
        
    def get_image_url(self, image):
        request = self.context.get('request')
        image_url = image.image.url
        return request.build_absolute_uri(image_url)
