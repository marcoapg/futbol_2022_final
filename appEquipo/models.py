from django.db import models

# Create your models here.

class categoria_equipo(models.Model):
    categoria_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        super(categoria_equipo, self).save(force_insert, force_update)
 
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural= 'categoria_equipo'


class tipo_equipo(models.Model):
    tipo_equipo_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(tipo_equipo, self).save(force_insert, force_update)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural='tipo_equipo'

class equipo(models.Model):
    equipo_id=models.BigAutoField(primary_key=True)
    logo=models.ImageField(null=True, blank=True, upload_to='equipo/logo/')
    vestimenta_principal=models.ImageField(null=True, blank=True, upload_to='equipo/vestimenta_principal/')
    vestimenta_alterna=models.ImageField(null=True,blank=True, upload_to='equipo/vestimenta_secundaria/')
    portada=models.ImageField(null=True,blank=True,upload_to='equipo/portada/')
    presidente=models.CharField(default='', max_length=50)
    nombre=models.CharField(max_length=70)
    siglas=models.CharField(max_length=3)
    categoria_equipo=models.ForeignKey(categoria_equipo,on_delete=models.CASCADE,db_column='categoria_equipo')
    tipo_equipo_id=models.ForeignKey(tipo_equipo,on_delete=models.CASCADE,db_column='tipo_equipo_id')
    sede_id=models.ForeignKey("appPartido.sede",on_delete=models.CASCADE,db_column='sede_id')
    deporte_id=models.ForeignKey("appCompeticion.deporte",on_delete=models.CASCADE,db_column='deporte_id')

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.siglas = self.siglas.upper()
        self.presidente = self.presidente.upper()
        super(equipo, self).save(force_insert, force_update)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='equipo'

class posicion_jugador(models.Model):
    posicion_jugador_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(posicion_jugador, self).save(force_insert, force_update)

    def __str__(self):
        return self.descripcion
        
    class Meta:
        verbose_name_plural='posicion_jugador'

class alineacion(models.Model):
    alineacion_id=models.BigAutoField(primary_key=True)
    fecha_juego=models.DateField()
    descripcion=models.CharField(max_length=50)
    estado=models.BooleanField()

    def __str__(self):
        return str(self.fecha_juego) + "-" + self.descripcion

    class Meta:
        verbose_name_plural='alineacion'


class alineacion_equipo(models.Model):
    alineacion_equipo_id=models.BigAutoField(primary_key=True)
    equipo_id=models.ForeignKey(equipo,on_delete=models.CASCADE,db_column='equipo_id')
    dorsal=models.IntegerField()
    posicion_jugador_id=models.ForeignKey(posicion_jugador,on_delete=models.CASCADE,db_column='posicion_jugador_id')
    capitan=models.BooleanField()
    estado=models.BooleanField()
    contrato_id=models.ForeignKey("appContrato.contrato",on_delete=models.CASCADE,db_column='contrato_id')
    alineacion_id=models.ForeignKey(alineacion,on_delete=models.CASCADE,db_column='alineacion_id')

    def __str__(self):
        return str(self.alineacion_equipo_id)
    
    class Meta:
        verbose_name_plural='alineacion_equipo'