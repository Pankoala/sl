from django.contrib import admin
from .models import Cliente, Tarjeta, ClienteTarjeta

class ClienteAdmin(admin.ModelAdmin):
    # Sobreescribe lo que se muestra #
    list_display = ("id", "user", "fechaNacimiento", "genero", "tipo")


class TarjetaAdmin(admin.ModelAdmin):
    list_display = ("nombreTarjeta", "descripcion", "interes")


class ClienteTarjetaAdmin(admin.ModelAdmin):
    list_display = ("numeroTarjeta", "cliente", "tarjeta", "creditoMax")


admin.site.register (Cliente, ClienteAdmin)
admin.site.register (Tarjeta, TarjetaAdmin)
admin.site.register (ClienteTarjeta, ClienteTarjetaAdmin)
