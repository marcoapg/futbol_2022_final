from django.contrib import admin
from appCompeticion.models import *

# Register your models here.
class tipo_competicionAdmin(admin.ModelAdmin):
    list_display=['tipo_competicion_id','nombre','estado']
    ordering=['tipo_competicion_id']
    search_fields = ['nombre']

class competicionAdmin(admin.ModelAdmin):
    list_display=['competicion_id','logo_competicion','deporte_id','nombre','pais_id','tipo_competicion_id']
    ordering=['competicion_id']
    search_fields = ['nombre']

class paisAdmin(admin.ModelAdmin):
    list_display=['pais_id','logo_bandera','nombre','sigla']
    ordering=['pais_id']
    search_fields = ['nombre']

class deporteAdmin(admin.ModelAdmin):
    list_display=['deporte_id','nombre','estado']
    ordering=['deporte_id']
    search_fields = ['nombre']

class grupoAdmin(admin.ModelAdmin):
    list_display=['grupo_id','slug','nombre']
    ordering=['grupo_id']
    search_fields = ['nombre']

class faseAdmin(admin.ModelAdmin):
    list_display=['fase_id','nombre']
    ordering=['fase_id']
    search_fields=['nombre']

class detalle_grupoAdmin(admin.ModelAdmin):
    list_display=['detalle_grupo_id','competicion_id','fase_id','grupo_id','equipo_id']
    ordering=['detalle_grupo_id']
    search_fields = ['equipo_id','grupo_id','competicion_id']


class tablaAdmin(admin.ModelAdmin):
    list_display=['tabla_id','competicion_id','equipo_id','ganado','perdido','empatado','goles_favor','goles_contra','tarjetas_amarillas','tarjetas_rojas','puntos']
    ordering=['tabla_id']
    earch_fields = ['competicion_id','equipo_id']

admin.site.register(tipo_competicion,tipo_competicionAdmin)
admin.site.register(competicion,competicionAdmin)
admin.site.register(pais,paisAdmin)
admin.site.register(deporte,deporteAdmin)
admin.site.register(grupo,grupoAdmin)
admin.site.register(fase,faseAdmin)
admin.site.register(detalle_grupo,detalle_grupoAdmin)
admin.site.register(tabla,tablaAdmin)