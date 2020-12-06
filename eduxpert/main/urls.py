from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^physics/$', views.physics, name='physics'),
    url(r'^chemistry/$', views.chemistry, name='chemistry'),
    url(r'^mathematics/$', views.mathematics, name='mathematics'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^contactUs.html/$', views.contact, name='contact'),
    url(r'^doubt/$', views.doubt, name='doubt'),
]