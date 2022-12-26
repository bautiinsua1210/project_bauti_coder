from django.contrib import admin
from django.urls import path, include
from AppCoder.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("AppCoder/", include("AppCoder.urls")),
    
]
