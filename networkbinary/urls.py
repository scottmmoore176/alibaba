
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [

 path('', views.index, name='index' ),
 path('ram', views.ram, name='ram' ),
 path('google', views.google, name='google' ),
 path('googlep', views.googlep, name='googlep' ),
 path('git', views.git, name='git' ),

]

