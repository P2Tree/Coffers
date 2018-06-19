from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.public_list, name='public_list'),
    url(r'^diary/$', views.post_list, name='post_list'),
    url(r'^diary/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^diary/new/$', views.post_new, name='post_new'),
    url(r'^diary/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^diary/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

]