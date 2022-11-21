from email.policy import default
from django.db import models
from django import forms

# Create your models here.

class pais(models.Model):
    pais_id=models.BigAutoField(primary_key=True)
    logo_bandera=models.ImageField(blank=True,null=True,upload_to='bandera/',default='bandera/bandera_default.png')
    nombre=models.CharField(max_length=30)
    sigla=models.CharField(max_length=3,default='')

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.sigla= self.sigla.upper()
        super(pais, self).save(force_insert, force_update)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name_plural='pais'

class tipo_competicion(models.Model):
    tipo_competicion_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    estado=models.BooleanField()
    
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(tipo_competicion, self).save(force_insert, force_update)

    def __str__(self):
         return str(self.nombre)

    class Meta:
        verbose_name_plural='tipo_competicion'

class deporte(models.Model):
    deporte_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    estado=models.BooleanField()

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(deporte, self).save(force_insert, force_update)

    def __str__(self):
         return str(self.deporte_id)
        
    class Meta: 
        verbose_name_plural='deporte'


class competicion(models.Model):
    competicion_id=models.BigAutoField(primary_key=True)
    logo_competicion=models.ImageField(null=True,blank=True,upload_to='competicion/logo/',default='competicion/logo/logo_default.png')
    nombre=models.CharField(max_length=50)
    pais_id=models.ForeignKey(pais,on_delete=models.CASCADE, db_column='pais_id')
    tipo_competicion_id=models.ForeignKey(tipo_competicion,on_delete=models.CASCADE, db_column='tipo_competicion_id')
    deporte_id=models.ForeignKey(deporte,on_delete=models.CASCADE, db_column='deporte_id')
    estado=models.BooleanField()
    fecha_inicio=models.DateField(blank=True,null=True,default='1990-12-12')
    fecha_fin=models.DateField(blank=True,null=True,default='1990-12-12')

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(competicion, self).save(force_insert, force_update)

    def __str__(self):
         return str(self.nombre)
    
    class Meta:
        verbose_name_plural='competicion'

class grupo(models.Model):
    grupo_id=models.BigAutoField(primary_key=True)
    slug=models.SlugField(blank=True,null=True)
    nombre=models.CharField(max_length=30)
    
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(grupo, self).save(force_insert, force_update)

    def __str__(self):
        return str(self.nombre)
    
    class Meta: 
        verbose_name_plural='grupo'

class fase(models.Model):
    fase_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(fase,self).save(force_insert, force_update)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name_plural='fase'


class detalle_grupo(models.Model):
    detalle_grupo_id=models.BigAutoField(primary_key=True)
    equipo_id=models.ForeignKey("appEquipo.equipo",on_delete=models.CASCADE, db_column='equipo_id')
    fase_id=models.ForeignKey(fase,on_delete=models.CASCADE, db_column='fase_id')
    grupo_id=models.ForeignKey(grupo,on_delete=models.CASCADE, db_column='grupo_id')
    competicion_id=models.ForeignKey(competicion,on_delete=models.CASCADE, db_column='competicion_id')

    def __str__(self):
        return str(self.detalle_grupo_id)
    
    class Meta: 
        verbose_name_plural='detalle_grupo'

class tabla(models.Model):
    tabla_id=models.BigAutoField(primary_key=True)
    competicion_id=models.ForeignKey(competicion,on_delete=models.CASCADE, db_column='competicion_id')
    equipo_id=models.ForeignKey("appEquipo.equipo",on_delete=models.CASCADE, db_column='equipo_id')
    ganado=models.IntegerField()
    perdido=models.IntegerField()
    empatado=models.IntegerField()
    goles_favor=models.IntegerField()
    goles_contra=models.IntegerField()
    tarjetas_amarillas=models.IntegerField()
    tarjetas_rojas=models.IntegerField()
    puntos=models.IntegerField()

    def __str__(self):
        return str(self.tabla_id)
    
    class Meta: 
        verbose_name_plural='tabla'
