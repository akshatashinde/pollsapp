from django.conf.urls import include,url
from django.contrib import admin
from notes import views

app_name='notes'
urlpatterns = [
    # url(r'^$',views.index, name='index'), 
    url(r'^home/$',views.home_view,name='home'),
    url(r'^$',views.index_view,name='index_view'),
    url(r'^addnote/$',views.add_note,name='add_note'),
    url(r'^addtag/$',views.add_tag,name='add_tag'),
    url(r'^tags/(?P<slug>[-\w]+)/$',views.tag_search, name='tagsearch'),

]
    