from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='landing'),
    url(r'^myaccount/$', views.mine, name='myaccount'),    url(r'^search/(?P<name>.+)$', views.find, name='save'),