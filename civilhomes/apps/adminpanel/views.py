from django.shortcuts import render
from django.views.generic import TemplateView
from civilhomes.apps.homepage.models import Companies, HomePageBasic, Service, VideoSection
from civilhomes.apps.imagegallery.models import Image
from civilhomes.apps.blogapp.models import Blog
from civilhomes.apps.projects.models import *


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
            company = Companies.objects.get(id=id)
            if companyName:
                company.name = companyName
            if companyLogo:
                imageObj = Image(image_name=request.POST.get('imageName'),image=companyLogo,image_type=request.POST.get('type'))
                imageObj.save()
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
            vid = VideoSection.objects.get(id=id)
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
            imageObj = Image.objects.get(id=id)
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
            blog = Blog.objects.get(id=id)
            if title:
                blog.title=title
            if content:
                blog.content=content
            if cover_image:
                imageObj = Image(image_name=request.POST.get('imageName'),image=cover_image,image_type=request.POST.get('type'))
                imageObj.save()
                blog.cover_image= imageObj
            blog.save()
        except :
            imageObj = Image(image_name=request.POST.get('imageName'),image=cover_image,image_type=request.POST.get('type'))
            imageObj.save()
            blog= Blog(title=title,content=content,cover_image=imageObj)
            blog.save()

class AddUpdateProject(TemplateView):

    def post(self, request, id,*args,**kwargs):
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        brochure_url =request.POST.get('brochure_url')
        project_plan = request.POST.get('project_plan')
        location = request.POST.get('location')
        try:
            project = Project.objects.get(id=id)
            if name:
                project.name=name
            if description:
                project.description=description
            if status:
                project.status=status
            if brochure_url:
                project.brochure_url=brochure_url
            if project_plan:
                project.project_plan=ProjectPlan.objects.get(id=project_plan)
            if location:
                project.location=Location.objects.get(id=location)
            project.save()

        except :
            project=Project(name = request.POST.get('name'),description = request.POST.get('description'),
                            status = request.POST.get('status'),
                            brochure_url =request.POST.get('brochure_url'),
                            project_plan = ProjectPlan.objects.get(id=project_plan),
                            location = Location.objects.get(id=location))
        project.save()


class ProjectInfo(TemplateView):

    def post(self, request, id,*args,**kwargs):
        project= request.POST.get('project')
        info= request.POST.get('info')
        value=request.POST.get('value')

        try:
            projectInfo= ProjectInfo.objects.get(id=id)

            if project:
                projectInfo.project=Project.objects.get(id=project)
            if info:
                info_ = Info(name=info)
                info_.save()
                projectInfo.info=info_
            if value:
                projectInfo.value=value
            projectInfo.save()
        
        except :
            info_ = Info(name=info)
            info_.save()
            projectInfo = ProjectInfo(project=Project.objects.get(id=project),
                                        info= info_,
                                        value=request.POST.get('value'))
            projectInfo.save()

class AddUpdateAmenities(TemplateView):

    def post(self, request, id,*args,**kwargs):
        name = request.POST.get('name')
        description = request.POST.get('description')
        project= request.POST.get('project')

        try:
            amenitie = Amenitie.objects.get(id=id)
            if name:
                amenitie.name = name
            if description:
                amenitie.description=description
            if project:
                amenitie.project=Project.objects.get(id=project)
            amenitie.save()
        
        except :
            amenitie = Amenitie(name = request.POST.get('name'),
                                description = request.POST.get('description'),
                                project= Project.objects.get(project))

class HomepageEdit(TemplateView):

    def post(self, request, id,*args,**kwargs):
        headerTitle= request.POST.get('headerTitle')
        headerDescription = request.POST.get('headerDescription')
        services = Service.objects.get.all()
        videoSection = request.POST.get('video')
        promotedProject = request.POST.get('project')
        ongoingProject = Project.objects.get.all()
        companies = Companies.objects.get.all()
        location = request.POST.get('location')
        contactInfo = request.POST.get('contact')
        try :
            homepage = HomePageBasic.objects.get(id=id)
            if headerTitle:
                homepage.headerTitle=headerTitle
            if headerDescription:
                homepage.headerDescription=headerDescription
            if videoSection:
                vid = VideoSection(videoTitle=request.POST.get('videoTitle'),video=request.FILES('video'),videoLink=request.POST.get('videoURL'))
                vid.save()
                homepage.videoSection = vid
            if promotedProject:
                homepage.promotedProject= Project.objects.get(id=promotedProject)
            if location:
                homepage.location = Location.objects.get(id=location)
            if contactInfo:
                homepage.contactInfo = contactInfo.objects.get(id=contactInfo)

            homepage.services = services
            homepage.ongoingProject = ongoingProject
            homepage.companies = companies
            homepage.save()
        except:
            homepage= HomePageBasic(headerTitle= request.POST.get('headerTitle'),
        headerDescription = request.POST.get('headerDescription'),
        services = Service.objects.get.all(),
        videoSection = request.POST.get('video'),
        promotedProject = request.POST.get('project'),
        ongoingProject = Project.objects.get.all(),
        companies = Companies.objects.get.all(),
        location = request.POST.get('location'),
        contactInfo = request.POST.get('contact'))
        homepage.save()
