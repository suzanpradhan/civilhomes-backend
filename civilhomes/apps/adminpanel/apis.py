from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from civilhomes.apps.imagegallery.models import Image
from django.http.response import HttpResponse, JsonResponse
from .serializers import ImageSerializer


class AddImage(APIView):
    
    def get(self, request, format=None):
        return None

    def post(self, request,*args,**kwargs):
        image_name=request.POST.get('image_name')
        image=request.FILES['image']
        image_type=request.POST.get('image_type')
        dimension=request.POST.get('dimension')
        

        imageObj = Image()
        if image_name:
            imageObj.image_name=image_name
        if image:
            imageObj.image=image
        if image_type:
            imageObj.image_type=image_type
        if dimension:
            imageObj.dimension = dimension
        imageObj.save()
        imageSaved = Image.objects.get(id=imageObj.pk)
        serializedImageObject = ImageSerializer(imageSaved, context={"request":request})
        #     "image_id": imageObj.pk,
        #     "image_name": imageSaved.name,
        #     "image_url": imageSaved.image.
        #     "image_type": imageSaved.image_type
        # }
        return JsonResponse(serializedImageObject.data)