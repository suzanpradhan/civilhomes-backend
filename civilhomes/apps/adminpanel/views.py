from civilhomes.apps import projects
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.http.response import HttpResponse, JsonResponse
from civilhomes.apps.homepage.models import Companies, ContactInfo, HomePageBasic, Service, VideoSection
from civilhomes.apps.imagegallery.models import Image
from civilhomes.apps.blogapp.models import Blog
from civilhomes.apps.projects.models import *
from django.http import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from json import dumps
from django.contrib import messages
from .serializers import ImageSerializer

class AdminLogin(TemplateView):
    template_name = "adminpanel/auth/login.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                messages.error(request,'Access Denied!')
                return redirect('admin-login')
        else:
            messages.error(request,'Bad Crendentials!')
            return redirect('admin-login')

def logoutAdminLogOut(request):
    logout(request)
    return redirect('admin-login')


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'adminpanel/dashboard.html'
    login_url = "admin-login"
    redirect_field_name = "hollaback"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class HomePageGeneralSettings(LoginRequiredMixin, TemplateView):
    template_name = "adminpanel/homepage/general_settings.html"
    login_url = "admin-login"
    redirect_field_name = "hollaback"

    def get(self, request, *args, **kwargs):
        homepageData = HomePageBasic.objects.first
        services = Service.objects.all()
        projects = Project.objects.all()
        context = {
            "homepageData":homepageData,
            "services": services,
            "projects": projects
        }
        return render(request, self.template_name, context=context)
    def post(self, request,*args, **kwargs):
        headerTitle = request.POST.get('header_title')
        header_description = request.POST.get('header_description')
        services = request.POST.getlist('services')
        promoted_project = request.POST.get('promoted_project')
        ongoing_projects = request.POST.getlist('ongoing_projects')
        youtube_video_link = request.POST.get('youtube_video_link')
        office_location = request.POST.get('office_location')
        office_contact_email = request.POST.get('office_contact_email')
        office_phone = request.POST.get('office_phone')
        office_fax = request.POST.get('office_fax')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        office_embed_map_snippet = request.POST.get('office_embed_map_snippet')

        homepageData = HomePageBasic.objects.first()
        homepageData.headerTitle = headerTitle
        homepageData.headerDescription = header_description
        if office_location:
            location=Location()
            location.name = office_location
            location.latitude = latitude
            location.longitude = longitude
            location.iframe_snippet = office_embed_map_snippet
            location.save()
            homepageData.location = location
        contactInfo=ContactInfo()
        contactInfo.address = office_location
        contactInfo.contactEmail = office_contact_email
        contactInfo.phone = office_phone
        contactInfo.fax = office_fax
        contactInfo.save()
        homepageData.contactInfo = contactInfo
        if youtube_video_link:
            videoSection=VideoSection()
            videoSection.videoLink = youtube_video_link
            videoSection.save()
            homepageData.videoSection = videoSection
        if promoted_project:
            promotedProjectObject = Project.objects.get(id=promoted_project)
            homepageData.promotedProject = promotedProjectObject
        homepageData.save()
        if services and len(services) > 0:
            for service in services:
                serviceObject = Service.objects.get(id=service)
                homepageData.services.add(serviceObject)
        if ongoing_projects and len(ongoing_projects) > 0:
            for ongoing_project in ongoing_projects:
                projectObject = Project.objects.get(id=ongoing_project)
                homepageData.ongoingProjects.add(projectObject)
        return redirect('admin-homepage-general-settings')

        

class AddUpdateCompany(TemplateView):
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
        video = request.FILES['video']
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

class ListDeleteVideo(TemplateView):
    
    def post(self, request,id,*args,**kwargs):
        VideoSection.objects.filter(id=id).delete()

    def get(self, request, *args, **kwargs):
        VideosAll = VideoSection.objects.all()

class AddImage(TemplateView):

    def post(self, request,*args,**kwargs):
        image_name=request.POST.get('image_name')
        
        image_type=request.POST.get('image_type')
        dimension=request.POST.get('dimension')

        imageObj = Image()
        if image_name:
            imageObj.image_name=image_name
        if 'image' in request.FILES:
            image=request.FILES['image']
            imageObj.image=image
        if image_type:
            imageObj.image_type=image_type
        if dimension:
            imageObj.dimension = dimension
        imageObj.save()
        imageSaved = Image.objects.get(id=imageObj.pk)
        serializedImageObject = ImageSerializer(imageSaved, context={"request":request})
        # jsonResponse = {
        #     "id": imageObj.pk,
        #     "image_name": imageSaved.name,
        #     "image_url": "sfghht",
        #     "image_type": imageSaved.image_type,
        # }
        return JsonResponse(serializedImageObject.data)


class ListDeleteImage(TemplateView):
    
    def post(self, request,id,*args,**kwargs):
        Image.objects.filter(id=id).delete()

    def get(self, request, *args, **kwargs):
        ImagesAll = Image.objects.all()

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

class AddProject(TemplateView):
    template_name ="adminpanel/projects/add_new_projects.html"

    def get(self, request,*args,**kwargs):
        status = (
            (1, "Not Started"),
            (2, "Ongoing"),
            (3, "Completed"),
            (4, "On Hold")
        )
        dimension = (
            (1, "2D"),
            (2, "3D")
        )
        image_types = (
            (1, "Ongoing"),
            (2, "Completed")
        )
        context = {
            "status": status,
            "dimensions": dimension,
            "image_types": image_types
        }
        
        return render(request,self.template_name, context)

    def post(self, request,*args,**kwargs):
        name = request.POST.get('project_name')
        description = request.POST.get('project_description')
        address = request.POST.get('project_location')
        
        project_status = request.POST.get('project_status')
        project_plan_name = request.POST.get('project_plan_name')
        

        amenities = request.POST.getlist('amenities[]')

        # project_video = request.FILES['project_video']
        project_video_youtube = request.POST.get('project_video_youtube')

        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        embed_map_snippet = request.POST.get('embed_map_snippet')

        project_images = request.POST.getlist('project_images[]')
        # try:
        project = Project()
        if name:
            project.name=name
        if description:
            project.description=description
        if project_status:
            project.status=project_status
        if 'project_brochure' in request.FILES:
            project_brochure = request.FILES['project_brochure']
            project.brochure_url=project_brochure
        if 'project_plan_file' in request.FILES:
            project_plan_file = request.FILES['project_plan_file']
            projectPlan=ProjectPlan(name=project_plan_name, sheet_url=project_plan_file)
            projectPlan.save()
            project.project_plan = projectPlan
        if address:
            location=Location()
            location.name = address
            location.latitude = latitude
            location.longitude = longitude
            location.iframe_snippet = embed_map_snippet
            location.save()
            project.location = location
        project.save()
        if amenities and len(amenities) > 0:
            for amenitie in amenities:
                amenitieObject = Amenitie.objects.get(id=amenitie)
                project.amenities.add(amenitieObject)
        if project_images and len(project_images) > 0:
            for image in project_images:
                imageObject = Image.objects.get(id=image)
                project.project_images.add(imageObject)
        return redirect('admin-project-all')

        # except :
        #     project=Project(name = request.POST.get('name'),description = request.POST.get('description'),
        #                     status = request.POST.get('status'),
        #                     brochure_url =request.POST.get('brochure_url'),
        #                     project_plan = ProjectPlan.objects.get(id=project_plan),
        #                     location = Location.objects.get(id=location))
        # project.save()

class UpdateProject(TemplateView):

    template_name ="adminpanel/projects/update_project.html"

    def get(self, request,id,*args,**kwargs):
        status = (
            (1, "Not Started"),
            (2, "Ongoing"),
            (3, "Completed"),
            (4, "On Hold")
        )
        dimension = (
            (1, "2D"),
            (2, "3D")
        )
        image_types = (
            (1, "Ongoing"),
            (2, "Completed")
        )
        project = Project.objects.get(id=id)
        context = {
            "status": status,
            "project":project,
            "dimensions": dimension,
            "image_types": image_types
        }
        
        return render(request,self.template_name, context)

    def post(self, request,id, *args,**kwargs):
        name = request.POST.get('project_name')
        description = request.POST.get('project_description')
        address = request.POST.get('project_location')
        
        project_status = request.POST.get('project_status')
        project_plan_name = request.POST.get('project_plan_name')
        

        amenities = request.POST.getlist('amenities[]')

        # project_video = request.FILES['project_video']
        # project_video_youtube = request.POST.get('project_video_youtube')

        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        embed_map_snippet = request.POST.get('embed_map_snippet')

        project_images = request.POST.getlist('project_images[]')
        # try:
        project = Project.objects.get(id=id)
        if name:
            project.name=name
        if description:
            project.description=description
        if project_status:
            project.status=project_status
        if 'project_brochure' in request.FILES:
            project_brochure = request.FILES['project_brochure']
            project.brochure_url=project_brochure
        if 'project_plan_file' in request.FILES:
            project_plan_file = request.FILES['project_plan_file']
            projectPlan=ProjectPlan(name=project_plan_name, sheet_url=project_plan_file)
            projectPlan.save()
            project.project_plan = projectPlan
        if address:
            location=Location()
            location.name = address
            location.latitude = latitude
            location.longitude = longitude
            location.iframe_snippet = embed_map_snippet
            location.save()
            project.location = location
        project.save()
        if amenities and len(amenities) > 0:
            for amenitie in amenities:
                amenitieObject = Amenitie.objects.get(id=amenitie)
                project.amenities.add(amenitieObject)
        if project_images and len(project_images) > 0:
            for image in project_images:
                imageObject = Image.objects.get(id=image)
                project.project_images.add(imageObject)
        return redirect('admin-project-all')

class ListProject(TemplateView):
    template_name ="adminpanel/projects/all_projects.html"

    def get(self, request, *args, **kwargs):
        ProjectAll = Project.objects.all()

        context = {
            "projects": ProjectAll
        }

        return render(request, self.template_name, context)

class DeleteProject(TemplateView):
    def get(self, request, id, *args, **kwargs):
        project = Project.objects.get(id=id)
        project.delete()
        return redirect("admin-project-all")



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

class ListDeleteProjectInfo(TemplateView):
    
    def post(self, request,id,*args,**kwargs):
        ProjectInfo.objects.filter(id=id).delete()

    def get(self, request, *args, **kwargs):
        ProjectInfoAll = ProjectInfo.objects.all()

class AddAmenitie(TemplateView):
    def post(self, request,*args,**kwargs):
        name = request.POST.get('amenitie_name')
        description = request.POST.get('amenitie_description')
        amenitie = Amenitie()
        if name:
            amenitie.name = name
        if description:
            amenitie.description=description
        amenitie.save()
        amenitieSaved = Amenitie.objects.get(id=amenitie.pk)
        jsonResponseData = {
            "amenitie_id": amenitie.pk,
            "amenitie_name": amenitieSaved.name,
            "amenitie_description": amenitieSaved.description
        }
        return JsonResponse(jsonResponseData)

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

class ListDeleteAmenities(TemplateView):
    
    def post(self, request,id,*args,**kwargs):
        Amenitie.objects.filter(id=id).delete()

    def get(self, request, *args, **kwargs):
        AmenitiesAll = Amenitie.objects.all()


class HomepageEdit(TemplateView):

    def post(self, request, id,*args,**kwargs):
        headerTitle= request.POST.get('headerTitle')
        headerDescription = request.POST.get('headerDescription')
        
        videoSection = request.POST.get('video')
        promotedProject = request.POST.get('project')
        
        location = request.POST.get('location')
        contactInfo = request.POST.get('contact')
        
        homepage = HomePageBasic.objects.get(id=id)
        services = homepage.services.all()
        ongoingProject = homepage.ongoingProject.all()
        companies = homepage.companies.all()
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
            homepage.contactInfo = ContactInfo.objects.get(id=contactInfo)

        homepage.services = services
        homepage.ongoingProject = ongoingProject
        homepage.companies = companies
        homepage.save()
