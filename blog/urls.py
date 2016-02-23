"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^category/(?P<category>[a-z]+)$', views.Category, name='check-category'),
    url(r'^tag-check$', views.Tag_ajax, name='tag-check'),
    url(r'^more$', views.More_ajax, name='more'),
    url(r'^(?P<blog_id>[0-9]+)$', views.Blog_content, name='con-blog'),
    url(r'^addlike$', views.Add_like, name='add-like'),
    url(r'^query$', views.Query_Blog, name='query'),

]
