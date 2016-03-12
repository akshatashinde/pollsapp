from django.conf.urls import include,url
from django.contrib import admin
from notes import views
from notes.views import tag_search
app_name='notes'
urlpatterns = [
    #url(r'^$',views.index, name='index'), 
    url(r'^$',views.home_view,name='home'),
    url(r'^addindex/$',views.index_view,name='index'),
    url(r'^addnote/$',views.add_note,name='addnote'),
    url(r'^addtag/$',views.add_tag,name='addtag'),
    url(r'^tags/(?P<slug>[-\w]+)/$', tag_search, name='tagsearch'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
]
    