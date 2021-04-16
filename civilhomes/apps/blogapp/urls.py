from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllBlogsPage.as_view(), name="all_blogs_page"),
    path('<int:id>', views.BlogDetail.as_view(), name="blog_detail_page")
]
