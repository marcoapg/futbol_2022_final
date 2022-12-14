# Generated by Django 4.1.1 on 2022-11-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appContrato', '0007_alter_persona_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fecha_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
