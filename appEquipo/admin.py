from django.contrib import admin
from appEquipo.models import *

# Register your models here.

class categoriaEquipo(admin.ModelAdmin):
    list_display=['categoria_id','nombre']
    ordering=['categoria_id']
    search_fields=['noxmbre']

class equipoAdmin(admin.ModelAdmin):
    list_display=['equipo_id','logo','vestimenta_principal','vestimenta_alterna','portada','presidente','nombre','siglas','categoria_equipo','tipo_equipo_id','sede_id','deporte_id']
    ordering=['equipo_id']
    search_fields = ['nombre']

class tipoEquipoAdmin(admin.ModelAdmin):
    list_display=['tipo_equipo_id','descripcion']
    ordering=['tipo_equipo_id']
    search_fields = ['descripcion']

class posicionJugadorAdmin(admin.ModelAdmin):
    list_display=['posicion_jugador_id','descripcion']
    ordering=['posicion_jugador_id']
    search_fields = ['descripcion']

class alineacionAdmin(admin.ModelAdmin):
    list_display=['alineacion_id','fecha_juego','descripcion','estado']
    ordering=['alineacion_id']
    search_fields=['descripcion']

class AlineacionEquipoAdmin(admin.ModelAdmin):
    list_display=['alineacion_equipo_id','equipo_id','dorsal','posicion_jugador_id','capitan','estado','contrato_id']
    ordering=['alineacion_equipo_id']
    search_fields = ['equipo_id']

admin.site.register(alineacion,alineacionAdmin)
admin.site.register(categoria_equipo,categoriaEquipo)
admin.site.register(tipo_equipo,tipoEquipoAdmin)
admin.site.register(equipo,equipoAdmin)
admin.site.register(posicion_jugador,posicionJugadorAdmin)
admin.site.register(alineacion_equipo,AlineacionEquipoAdmin)
