from django.contrib import admin
from appContrato.models import *

# Register your models here.
class tipo_personaAdmin(admin.ModelAdmin):
    list_display = ['tipo_persona_id', 'descripcion', 'estado']
    ordering = ['tipo_persona_id']
    search_fields = ['descripcion']

class personaAdmin(admin.ModelAdmin):
    list_display=['persona_id', 'nombre', 'apellido', 'alias', 'sexo', 'fecha_nacimiento','ciudad_id','estatura','peso','estado','tipo_persona_id','foto']
    ordering = ['persona_id']
    search_fields = ['nombre','apellido','alias']

class contratoAdmin(admin.ModelAdmin):
    list_display=['contrato_id', 'fecha_inicio', 'fecha_fin', 'valor', 'tipo_contrato','persona_id','ultimo_club','nuevo_club','posicion_jugador','dorsal','estado']
    ordering = ['contrato_id']
    search_fields = ['equipo_id', 'persona_id']

admin.site.register(tipo_persona,tipo_personaAdmin)
admin.site.register(persona,personaAdmin)
admin.site.register(contrato,contratoAdmin)
