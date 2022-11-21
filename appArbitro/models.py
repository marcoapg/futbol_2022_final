from tabnanny import verbose
from django.db import models

# Create your models here.

class arbitro(models.Model):

    CHOICE_TIPO_ARBITRO = [
        ('P','PRINCIPAL'),
        ('J','JUEZ DE LINEA'),
        ('C','CUARTO HOMBRE'),
        ('V','VAR'),
    ]

    arbitro_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField()
    # CHOICE_TIPO_ARBITRO | P = Principal , J = Juez de Linea | C = Cuarto Hombre | V = Var
    tipo_arbitro=models.CharField(max_length=1, choices=CHOICE_TIPO_ARBITRO, default='P')
    pais_id=models.ForeignKey("appCompeticion.pais",on_delete=models.CASCADE,db_column='pais_id')
    estado=models.BooleanField()

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.apellido= self.apellido.upper()
        super(arbitro, self).save(force_insert, force_update)

    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        verbose_name_plural='arbitro'
        
class tipo_terna(models.Model):

    tipo_terna_id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    siglas = models.CharField(max_length=3)

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        self.siglas = self.siglas.upper()
        super(tipo_terna, self).save(force_insert, force_update)

    def __str__(self):
        return str(self.descripcion)
    
    class Meta:
        verbose_name_plural='tipo_terna'

class terna_arbitral(models.Model):
    terna_arbitral_id=models.BigAutoField(primary_key=True)
    nombre_terna=models.CharField(max_length=50)
    estado=models.BooleanField()
    
    def save(self, force_insert=False, force_update=False):
        self.nombre_terna = self.nombre_terna.upper()
        super(terna_arbitral, self).save(force_insert, force_update)
    def __str__(self):
        return self.nombre_terna

    class Meta:
        verbose_name_plural='terna_arbitral'

class detalle_terna(models.Model):
    detalle_terna_id=models.BigAutoField(primary_key=True)
    terna_arbitral_id=models.ForeignKey(terna_arbitral,on_delete=models.CASCADE,db_column='terna_arbitral_id')
    tipo_terna_id=models.ForeignKey(tipo_terna,on_delete=models.CASCADE,db_column='tipo_terna_id')
    arbitro_id=models.ForeignKey(arbitro,on_delete=models.CASCADE,db_column='arbitro_id')
    estado_juego=models.BooleanField()

    def __str__(self):
        return str(self.terna_arbitral_id)

    class Meta:
        verbose_name_plural='detalle_terna'

