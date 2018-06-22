"""bespinglobal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'bspmanager'
    

urlpatterns = [
    url('index/', views.index, name = 'index'),
    #url(r'^(?P<service_id>\d+)/$', views.viewdetails, name='viewdetails'),
    #url(r'^post/$', views.post, name = 'post'),
    #url(r'^change/(?P<service_id>\d+)/$', views.change, name = 'change'),
    #url(r'^delpost/(?P<service_id>\d+)/$', views.delpost, name = 'delpost'),
    #url(r'^company/$', views.companyindex, name= 'companyindex'),
    #url(r'^company/(?P<company_name>.+)/$', views.viewcompanydetails, name='viewcompanydetails'),
    url(r'^', views.scheduleindex, name='scheduleindex'),
]