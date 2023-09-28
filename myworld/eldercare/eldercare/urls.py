from django.contrib import admin
from django.urls import include, path
from data import views

urlpatterns = [
    path('', include('data.urls')),
    path('admin/', admin.site.urls),
    path('dataimport/',views.upload),
    path('map/', views.map_view, name='map'),
    path('map/uploadmapdata/', views.uploadmapdata, name='uploadmapdata'),
    path('cleardata/', views.cleardata, name='cleardata'),
    path('refresh_table/', views.refresh_table, name='refresh_table'),
    path('map/filter_sort/', views.filter_sort_view, name='filter_sort'),
]