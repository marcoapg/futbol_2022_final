# Generated by Django 4.1.1 on 2022-11-14 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appEquipo', '0010_alter_alineacion_options_and_more'),
        ('appPartido', '0010_encuentro_equipo_local_encuentro_equipo_visita_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuentro',
            name='alineacion_local',
            field=models.ForeignKey(db_column='alineacion_local', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='alineacion_local', to='appEquipo.alineacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='encuentro',
            name='alineacion_visita',
            field=models.ForeignKey(db_column='alineacion_visita', default=2, on_delete=django.db.models.deletion.CASCADE, related_name='alineacion_visita', to='appEquipo.alineacion'),
            preserve_default=False,
        ),
    ]
