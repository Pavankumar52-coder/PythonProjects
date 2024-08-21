from django.contrib import admin
from django.urls import path
from Images import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.image_upload, name='image_upload'),
    path('', views.image_upload, name='image_list'),
]