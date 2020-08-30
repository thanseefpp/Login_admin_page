from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('home',views.home,name="home"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('adminpanel',views.adminpanel,name="adminpanel")
]