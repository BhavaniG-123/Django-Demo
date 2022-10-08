from django.contrib import admin
from django.urls import path
from DemoApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login),
    path('loginData/', verify),
    path('logout/', logout),
    path('register/', register),
    path('register_data/', register_data),
]
