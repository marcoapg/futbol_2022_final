# Generated by Django 4.1.1 on 2022-09-30 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appEquipo', '0001_initial'),
        ('appPartido', '0001_initial'),
        ('appContrato', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='sede_id',
            field=models.ForeignKey(db_column='sede_id', on_delete=django.db.models.deletion.CASCADE, to='appPartido.sede'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='tipo_equipo_id',
            field=models.ForeignKey(db_column='tipo_equipo_id', on_delete=django.db.models.deletion.CASCADE, to='appEquipo.tipo_equipo'),
        ),
        migrations.AddField(
            model_name='alineacion_equipo',
            name='contrato_id',
            field=models.ForeignKey(db_column='contrato_id', on_delete=django.db.models.deletion.CASCADE, to='appContrato.contrato'),
        ),
        migrations.AddField(
            model_name='alineacion_equipo',
            name='equipo_id',
            field=models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='appEquipo.equipo'),
        ),
        migrations.AddField(
            model_name='alineacion_equipo',
            name='posicion_jugador_id',
            field=models.ForeignKey(db_column='posicion_jugador_id', on_delete=django.db.models.deletion.CASCADE, to='appEquipo.posicion_jugador'),
        ),
    ]
