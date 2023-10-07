from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #TODO: Admin Portal: Make it so admin redirects to a page that tells the user it would be only allowed for users on the WAN.
    path('admin/', admin.site.urls),
    path('',include('google.urls')),
]
