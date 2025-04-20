from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.new),
    path('romeiro/', views.romeiro_view, name='romeiro'),
    path('empty/', views.empty_island_view, name='empty_island'),
    path('light/', views.light_path_view, name='light_path'),
    path('sunset/', views.sunset_view, name='sunset'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)