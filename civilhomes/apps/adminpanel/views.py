from django.shortcuts import render
from django.views.generic import TemplateView
from civilhomes.apps.homepage.models import Companies, VideoSection
from civilhomes.apps.imagegallery.models import Image
from civilhomes.apps.blogapp.models import Blog


class Dashboard(TemplateView):
    template_name = 'adminpanel/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class HomePageGeneralSettings(TemplateView):
    template_name = "adminpanel/homepage/general_settings.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class AddUpdateComapany(TemplateView):

    def post(self, request,id,*args, **kwargs):
        companyName = request.POST.get('companyName')
        companyLogo = request.FILES.get('image')
        try:
            company = Companies.objects.get(id)
            if companyName:
                company.name = companyName
            if companyLogo:
                imageObj = Image(image_name=request.POST.get('imageName'),image=companyLogo,image_type=request.POST.get('type'))
                company.companyLogo = imageObj
            company.save()
        except:
            imageObj = Image(image_name=request.POST.get('imageName'),image=companyLogo,image_type=request.POST.get('type'))
            imageObj.save()
            company.companyLogo = imageObj
            company = Companies(name=companyName,companyLogo=companyLogo)
            company.save()

class ListDeleteCompanies(TemplateView):
    
    def post(self, request,id,*args,**kwargs):
        Companies.objects.filter(id=id).delete()

    def get(self, request, *args, **kwargs):
        companiesAll = Companies.objects.all()

class AddUpdateVideo(TemplateView):

    def post(self, request,id,*args,**kwargs):
        videoTitle = request.POST.get('videoTitle')
        video = request.FILES('video')
        videoURL= request.POST.get('videoURL')

        try:
            vid = VideoSection.objects.get(id)
            if videoTitle:
                vid.videoTitle = videoTitle
            if video:
                vid.video = video
            if videoURL:
                vid.videoLink=videoURL
            vid.save()
        except :
            vid = VideoSection(videoTitle=videoTitle,video=video,videoLink=videoURL)
            vid.save()

class AddUpdateImages(TemplateView):

    def post(self, request,id,*args,**kwargs):
        image_name=request.POST.get('imageName')
        image=request.FILES('image')
        image_type=request.POST.get('type')

        try:
            imageObj = Image.objects.get(id)
            if image_name:
                imageObj.image_name=image_name
            if image:
                imageObj.image=image
            if image_type:
                imageObj.image_type=image_type
            imageObj.save()
        except :
            imageObj=Image(image_name=request.POST.get('imageName'),image=request.FILES('image'),image_type=request.POST.get('type'))
            imageObj.save()

class ListDeleteBlog(TemplateView):

    def post(self, request,id,*args,**kwargs):
        Blog.objects.filter(id=id).delete()

    def get(self, request, *args, **kwargs):
        blogAll = Blog.objects.all()

class AddUpdateBlog(TemplateView):

    def post(self, request,id,*args,**kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        cover_image = request.FILES('image')
        date= request.POST.get('date')

        try:
            blog = Blog.objects.get(id)
            if title:
                blog.title=title
            if content:
                blog.content=content
            if cover_image:
                imageObj = Image(image_name=request.POST.get('imageName'),image=cover_image,image_type=request.POST.get('type'))
                blog.cover_image= imageObj
            ##date aafai add hunna ra save() garda?
            blog.save()
        except :
            imageObj = Image(image_name=request.POST.get('imageName'),image=cover_image,image_type=request.POST.get('type'))
            imageObj.save()
            blog= Blog(title=title,content=content,cover_image=imageObj)
            blog.save()
            