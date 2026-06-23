from django.contrib import admin

from ordenamiento.models import Parroquia, BarrioCiudadela, PresidenteBarrio


class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre', 'ubicacion', 'tipo')

admin.site.register(Parroquia, ParroquiaAdmin)


class BarrioCiudadelaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'numero_viviendas',
        'numero_parques',
        'numero_edificios_residenciales',
        'parroquia'
    )
    search_fields = ('nombre',)
    raw_id_fields = ('parroquia',)

admin.site.register(BarrioCiudadela, BarrioCiudadelaAdmin)


class PresidenteBarrioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nickname', 'edad', 'profesion', 'barrio')
    search_fields = ('cedula', 'nickname', 'profesion')
    raw_id_fields = ('barrio',)

admin.site.register(PresidenteBarrio, PresidenteBarrioAdmin)