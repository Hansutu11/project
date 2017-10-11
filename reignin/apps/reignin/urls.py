from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^reignin/log_reg$', views.log_reg),
    url(r'^reignin/login$', views.login),
    url(r'^reignin/register$', views.register),
    url(r'^reignin/success$', views.success),
]
