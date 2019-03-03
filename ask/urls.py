from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ask_list, name='ask_list'),
]
