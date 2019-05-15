from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^login/$', login, {'template_name': 'loginPage/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'loginPage/logout.html'}),
    url(r'^register/$', views.register, name='register'),
]