from django.shortcuts import render
from django.views.generic import TemplateView
from . import models as blog_models

class AllBlogsPage(TemplateView):
    template_name = "newsroom/index.html"

    def get(self, request, *args, **kwargs):
        blogs = blog_models.Blog.objects.all()
        context = {
            "blogs": blogs
        }
        return render(request, self.template_name, context)

class BlogDetail(TemplateView):
    template_name = 'newsroom/detail_page.html'

    def get(self, request,id, *args, **kwargs):
        blog = blog_models.Blog.objects.get(id=id)
        context = {
            "blog": blog
        }
        return render(request, self.template_name, context)
