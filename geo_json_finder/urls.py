from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lines$', views.lines, name='lines'),
    url(r'^locations$', views.locations, name='locations'),
]
