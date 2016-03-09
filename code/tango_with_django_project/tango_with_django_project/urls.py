"""tango_with_django_project URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from rango import views
from registration.backends.simple.views import RegistrationView 

class MyRegistrationView(RegistrationView):
        def get_success_url(self,request,user):
            return '/rango/'


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^rango/',include('rango.urls')),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^about/$',views.about,name='about'),
    url(r'^link/$', views.link, name='link'),
    url(r'^goto/$',views.track_url, name='goto'),
    url(r'^like_category/$',views.like_category, name='like_category'),
    url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
    #url(r'^category$',views.category, name='category'),
    url(r'^category/$',views.add_category, name='add_category'),
    url(r'^add_page/(?P<slug>[\W]+)/$', views.add_page,name='add_page'),
    url(r'^register/$', views.register,name='register'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^restricted/',views.restricted,name='restricted'),
    url(r'^logout/$',views.user_logout,name='logout')
]
