from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('post/<slug>/', views.post),
    path('', views.index),
    url(r'^admin/', admin.site.urls),
]
