from django.conf.urls import url
from . import views

urlpatterns=[
  url(r'^$', views.index, name='index'),
  url(r'^search/', views.search_results, name='search'),
  url(r'^location/(?P<location>\w+', views.image_location, name='location'),
]