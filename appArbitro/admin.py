from django.contrib import admin
from appArbitro.models import *

# Register your models here.

class arbitroAdmin(admin.ModelAdmin):
    list_display=['arbitro_id','nombre','apellido','tipo_arbitro','pais_id','estado']
    ordering=['arbitro_id']
    search_fields = ['nombre','apellido']

class tipoTernaAdmin(admin.ModelAdmin):
    list_display=['tipo_terna_id','descripcion','siglas']
    ordering=['tipo_terna_id']
    search_fields = ['descripcion','siglas']

class ternaArbitralAdmin(admin.ModelAdmin):
    list_display=['terna_arbitral_id','nombre_terna','estado']
    ordering=['terna_arbitral_id']
    search_fields = ['nombre_terna']

class detalleTernaArbitralAdmin(admin.ModelAdmin):
    list_display=['detalle_terna_id','terna_arbitral_id','arbitro_id','tipo_terna_id','estado_juego']
    ordering=['detalle_terna_id']
    search_fields = ['terna_arbitral_id','arbitro_id']

admin.site.register(arbitro,arbitroAdmin)
admin.site.register(tipo_terna,tipoTernaAdmin)
admin.site.register(terna_arbitral,ternaArbitralAdmin)
admin.site.register(detalle_terna,detalleTernaArbitralAdmin)