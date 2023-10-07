from .views import *
from django.urls import path, include
from google import views as view

urlpatterns = [
   path('',view.map, name="home"),
   path('mydata',view.mydata, name="mydata"),
]