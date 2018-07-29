from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='landing'),
    url(r'^myaccount/$', views.mine, name='myaccount'),
    url(r'^myaccount/edit/$', views.edit, name='edit'),
    url(r'^comment/(?P<post_id>\d+)$', views.comment_on, name='comment'),