from django.db import models
from django.db.models.functions import Upper
from project.settings import MEDIA_URL, STATIC_URL
# Create your models here.

class tipo_persona(models.Model):
    tipo_persona_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(tipo_persona, self).save(force_insert, force_update)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural='tipo_persona'


class persona(models.Model):

    CHOICE_SEXO = [
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
    ]

    persona_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    alias=models.CharField(max_length=30)
    # CHICE_SEXO | M = Masculino , F = Femenino
    sexo=models.CharField(max_length=1,choices=CHOICE_SEXO, default='M')
    fecha_nacimiento=models.DateField()
    ciudad_id=models.ForeignKey("appPartido.ciudad",on_delete=models.CASCADE, db_column='ciudad_id')
    estatura=models.FloatField()
    peso=models.FloatField()
    estado=models.BooleanField()
    tipo_persona_id=models.ForeignKey(tipo_persona,on_delete=models.CASCADE, db_column='tipo_persona_id')
    foto = models.ImageField(null=True,blank=True, upload_to='jugador/foto/', default='jugador/def_jugador.png')
    #Guardar en mayùscula
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.alias = self.alias.upper()
        super(persona, self).save(force_insert, force_update)
 
    def __str__(self):
        return self.nombre + ' ' + self.apellido

    def get_foto(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(STATIC_URL, 'jugador/def_jugador.png')

    class Meta:
        verbose_name_plural='persona'

class contrato(models.Model):

    CHOICE_TIPO_CONTRATO = [
        ('P','PRÉSTAMO'),
        ('C','COMPRA'),
        ('L','LIBRE'),
        ('R','RENOVACIÓN'),
        ('S','SELECCIÓN'),
    ]

    contrato_id=models.BigAutoField(primary_key=True)
    fecha_inicio=models.DateField(blank=True,null=True)
    fecha_fin=models.DateField(blank=True,null=True)
    valor=models.FloatField(blank=True,null=True) 
    # CHOICE_TIPO_CONTRATO | P = Prestamo , C = Compra , L = Libre , S = Seleccion , Renovacion
    tipo_contrato=models.CharField(max_length=1, choices=CHOICE_TIPO_CONTRATO, default='C')
    persona_id=models.ForeignKey(persona,on_delete=models.CASCADE, db_column='persona_id')
    ultimo_club=models.ForeignKey('appEquipo.equipo',on_delete=models.CASCADE,db_column='ultimo_club',related_name='ultimo_club',null=True,blank=True)
    nuevo_club=models.ForeignKey('appEquipo.equipo',on_delete=models.CASCADE,db_column='nuevo_club',related_name='nuevo_club',null=True,blank=True)
    dorsal=models.IntegerField(blank=True, null=True)
    posicion_jugador=models.CharField(max_length=30, blank= True, null=True)
    estado=models.BooleanField()

    def save(self, force_insert=False, force_update=False):
        self.posicion_jugador = self.posicion_jugador
        super(contrato, self).save(force_insert, force_update)
        
    def __str__(self):
        return str(self.persona_id)

    class Meta:
        verbose_name_plural='contrato'