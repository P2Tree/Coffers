from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^qiandao/(?P<complete>[0-1]+)/$', views.qiandao, name='qiandao'),
    url(r'^$', views.help, name='help'),
    url(r'^check/$', views.manual_check, name='manual_check')

]
