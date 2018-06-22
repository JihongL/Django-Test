from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic.base import TemplateView


from django.conf.urls.static import static
from django.conf import settings
from bspmanager import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bspmanager/', include('bspmanager.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [url(r'^', views.scheduleindex, name='scheduleindex'),] 