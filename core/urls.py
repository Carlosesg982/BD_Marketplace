from django.urls import path
from .views import home, nosotros, products, register, exit, perfil, publicar, Ventas_Publicadas


urlpatterns = [
    path('', home, name='home'),
    path('nosotros/',nosotros, name='nosotros'),
    path('perfil/',perfil, name='perfil'),
    path('Ventas_Publicadas/',Ventas_Publicadas, name='Ventas_Publicadas'),
    path('publicar/',publicar, name='publicar'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
]