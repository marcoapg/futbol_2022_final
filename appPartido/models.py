from email.policy import default
from random import choices
from django.db import models
from django import forms

# Create your models here.
class formacion(models.Model):
    formacion_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=10)

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(formacion, self).save(force_insert, force_update)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural='formacion'

class estado(models.Model):
    estado_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(estado, self).save(force_insert, force_update)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='estado'

class ciudad(models.Model):
    ciudad_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    norma=models.CharField(max_length=5)
    pais_id=models.ForeignKey('appCompeticion.pais',on_delete=models.CASCADE,db_column='pais_id')

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.norma = self.norma.upper()
        super(ciudad, self).save(force_insert, force_update)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='ciudad'

class sede(models.Model):
    CHOICE_ESTADO_SEDE=[
        ('SD','SUSPENDIDO DEFINITIVAMENTE'),
        ('DI','DISPONIBLE'),
        ('EM','EN MANTENIMIENTO'),
        ('ND','NO DISPONIBLE'),
        ('ST','SUSPENDIDO TEMPORALMENTE')
    ]
    sede_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    alias=models.CharField(max_length=50)
    capacidad=models.IntegerField()
    fecha_inauguracion=models.DateField()
    ciudad_id=models.ForeignKey(ciudad, on_delete=models.CASCADE,db_column='ciudad_id')
    # CHOICE_ESTADO_SEDE| SD= SUSPENDIDO TEMPORALMENTE, DI= DISPONIBLE , EM = EN MANTENIMIENTO, ND = NO DISPONIBLE, ST = SUSPENDIDO TEMPORALMENTE
    estado=models.CharField(max_length=2,default='DI',choices=CHOICE_ESTADO_SEDE)

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.alias = self.alias.upper()
        super(sede, self).save(force_insert, force_update)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='sede'


class encuentro(models.Model):
    CHOICE_RESULTADO = [
        ('G', 'GANADO'),
        ('E', 'EMPATADO'),
        ('P', 'PERDIDO'),
    ]

    encuentro_id=models.BigAutoField(primary_key=True)
    fase=models.ForeignKey("appCompeticion.fase", on_delete=models.CASCADE,db_column='fase',related_name='fase')
    grupo=models.ForeignKey("appCompeticion.grupo", on_delete=models.CASCADE,db_column='grupo',related_name='grupo')
    alineacion_local=models.ForeignKey("appEquipo.alineacion",on_delete=models.CASCADE,db_column='alineacion_local',related_name='alineacion_local',blank=True,null=True)
    alineacion_visita=models.ForeignKey("appEquipo.alineacion",on_delete=models.CASCADE,db_column='alineacion_visita',related_name='alineacion_visita',blank=True,null=True)
    equipo_local=models.ForeignKey('appEquipo.equipo', on_delete=models.CASCADE,db_column='equipo_local',related_name='equipo_local')
    equipo_visita=models.ForeignKey('appEquipo.equipo', on_delete=models.CASCADE,db_column='equipo_visita',related_name='equipo_visita')
    formacion_local=models.ForeignKey('formacion',on_delete=models.CASCADE,db_column='formacion_local',related_name='formacion_local',blank=True,null=True)
    formacion_visita=models.ForeignKey('formacion',on_delete=models.CASCADE,db_column='formacion_visita',related_name='formacion_visita',blank=True,null=True)
    # CHOICE FIELD | G = GANADO , E = EMPATADO , P = PERDIDO
    resultado_local=models.CharField(max_length=1,choices=CHOICE_RESULTADO)
    resultado_visita=models.CharField(max_length=1,choices=CHOICE_RESULTADO)
    resultado_goles_local=models.IntegerField() #2
    resultado_goles_visita=models.IntegerField() #0
    competicion_id=models.ForeignKey("appCompeticion.competicion", on_delete=models.CASCADE,db_column='competicion_id')
    sede_id=models.ForeignKey(sede,on_delete=models.CASCADE,db_column='sede_id',blank=True,null=True)
    terna_arbitral_id=models.ForeignKey("appArbitro.terna_arbitral", on_delete=models.CASCADE,db_column='terna_arbitral_id')
    fecha=models.DateTimeField(blank=True,null=True)
    humedad=models.CharField(max_length=4)
    clima=models.CharField(max_length=4)
    estado_jugado=models.BooleanField()

    def save(self, force_insert=False, force_update=False):
        self.humedad = self.humedad.upper()
        self.clima = self.clima.upper()
        self.resultado_local = self.resultado_local.upper()
        self.resultado_visita = self.resultado_visita.upper()
        super(encuentro, self).save(force_insert, force_update)

    def __str__(self):
        return str(self.encuentro_id)
    
    class Meta:
        verbose_name_plural='encuentro'

# class detalle_encuentro(models.Model):
#     CHOICE_TIPO_EQUIPO= [
#         ('L','LOCAL'),
#         ('V','VISITA'),
#     ]

#     detalle_encuentro_id=models.BigAutoField(primary_key=True)
#     encuentro_id=models.ForeignKey('encuentro',on_delete=models.CASCADE,db_column='encuentro_id')
#     equipo_id=models.ForeignKey('appEquipo.equipo', on_delete=models.CASCADE,db_column='equipo_id')
#     formacion_id=models.ForeignKey('formacion',on_delete=models.CASCADE,db_column='formacion_id')
#     # CHOICE_TIPO_EQUIPO | L = LOCAL | V = VISITA
#     tipo_equipo=models.CharField(max_length=1,choices=CHOICE_TIPO_EQUIPO)
#     resultado=models.CharField(max_length=3)

#     def __str__(self):
#         return str(self.detalle_encuentro_id)

#     class Meta:
#         verbose_name_plural='detalle_encuentro'
    
class evento(models.Model):
    evento_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(evento, self).save(force_insert, force_update)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural='evento'

class evento_persona(models.Model):
    CHOICE_TIPO_SUCESO= [
        ('E','ENTRADA'),
        ('S','SALIDA'),
    ]

    encuentro_evento_id=models.BigAutoField(primary_key=True)
    encuentro_id=models.ForeignKey(encuentro,on_delete=models.CASCADE,db_column='encuentro_id')
    evento_id=models.ForeignKey(evento,on_delete=models.CASCADE,db_column='evento_id')
    persona_id=models.ForeignKey("appContrato.persona",on_delete=models.CASCADE,db_column='persona_id')
    suceso=models.CharField(max_length=5,default='ABC')
    # CHOICE_TIPO_SUCESO | E = ENTRADA , S = SALIDA
    tipo_suceso=models.CharField(max_length=1,choices=CHOICE_TIPO_SUCESO,blank=True,null=True)   
    tiempo=models.IntegerField()
    observacion=models.CharField(max_length=50,blank=True,null=True)

    def save(self, force_insert=False, force_update=False):
        self.suceso = self.suceso.upper()
        self.observacion = self.observacion.upper()
        super(evento_persona, self).save(force_insert, force_update)

    def __str__(self):
        return str(self.encuentro_evento_id)

    class Meta:
        verbose_name_plural='evento_persona'

