# Generated by Django 4.1.1 on 2022-10-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEquipo', '0003_remove_equipo_vestimenta_equipo_vestimenta_alterna_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='presidente',
            field=models.CharField(default='', max_length=50),
        ),
    ]
