# Generated by Django 4.1.1 on 2022-11-14 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCompeticion', '0012_grupo_slug'),
        ('appPartido', '0014_alter_encuentro_sede_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuentro',
            name='fase',
            field=models.ForeignKey(db_column='fase', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fase', to='appCompeticion.fase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='encuentro',
            name='grupo',
            field=models.ForeignKey(db_column='grupo', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='grupo', to='appCompeticion.grupo'),
            preserve_default=False,
        ),
    ]