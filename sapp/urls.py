
from django.conf.urls import url
from . import views

urlpatterns=[
    url('home/',views.home,name="home"),
    url('about/',views.about,name="about"),
]