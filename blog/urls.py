from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.blogs , name='blog'),
    path('<slug:slug>', views.blog_detail , name='blog-detail'),

]