"""
URL configuration for smartcityconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from smartcity.views import *
from django.urls import path, include

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('CustomerReg/',CustomerReg,name='CustomerReg'),
    path('ServiceproviderReg/',ServiceproviderReg,name='ServiceproviderReg'),
    path('Login_page/',Login_page,name='Login_page'),
    path('Plumber/',Plumber,name="Plumber"),
    path('electrition/',electrition,name="electrition"),
    path('Home/',Home,name='Home'),
    path('logout/', logout_view, name='logout'), 
    path('carpenter/',carpenter,name="carpenter"),
    path('painters/',painters,name='painters'),
    path('Welding/',welding,name='Welding'),
    path('Cableprovider/',Cableprovider,name='Cableprovider'),
    path('Internet/',Internet,name='Internet'),
    path('Groceries/',Groceries,name="Groceries")
   
    
]
