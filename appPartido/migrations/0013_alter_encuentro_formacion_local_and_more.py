# Generated by Django 4.1.1 on 2022-11-14 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPartido', '0012_alter_encuentro_alineacion_local_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuentro',
            name='formacion_local',
            field=models.ForeignKey(blank=True, db_column='formacion_local', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formacion_local', to='appPartido.formacion'),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='formacion_visita',
            field=models.ForeignKey(blank=True, db_column='formacion_visita', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formacion_visita', to='appPartido.formacion'),
        ),
    ]
