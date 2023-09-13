
from django.contrib import admin
from django.urls import path
from restaurants import views
from django.views.generic import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/map_link/', views.map_link, name='map_link'),
    path('api/route_link/', views.route_link, name='route_link'),
    path('api/roadview_link/', views.roadview_link, name='roadview_link'),
    path('api/search_link/', views.search_link, name='search_link'),
    path('', views.secret, name='map_test'),
    path('api/geocode/', views.geocode_address, name='geocode_address'),


]
