from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca-de/', views.acerca_de, name="acerca_de"),
    path('contacto/', views.contacto, name="contacto"),
    path('servicios/', views.servicios, name="servicios"),
    path('tarjetas/', views.tarjetas, name="tarjetas"),
    path('portal/', views.portal, name="portal"),
    path('login/', views.login_usuario, name="login"),
    path('logout/', views.logout_usuario, name="logout"),
]

