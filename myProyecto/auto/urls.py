from django.contrib import admin
from django.urls import path
 #<--incluir ubicasion archivo-->
from .views import home,nosotros,productos,contacto

urlpatterns = [
    path('',home,name='HOME'),
    path('productos/',productos,name='PRODUC'),
    path('nosotros/',nosotros,name='NOSOT'),
    path('contacto/',contacto,name='CONTACT'),
   
]