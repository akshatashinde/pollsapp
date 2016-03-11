"""djangonote URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
# from notes import views


urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    # url(r'^notes/',include('notes.urls')),
    url(r'^notes/', include('notes.urls', namespace='notes')),
    # url(r'^$',views.index, name='index'),
    # url(r'^$',views.home_view,name='home'),
    # url(r'^addindex/$',views.index_view,name='index_view'),
    # url(r'^addnote/$',views.add_note,name='add_note'),
    # url(r'^addtag/$',views.add_tag,name='add_tag'),
    # url(r'^tags/(?P<slug>[-\w]+)/$',views.tag_search, name='tagsearch'),

]
