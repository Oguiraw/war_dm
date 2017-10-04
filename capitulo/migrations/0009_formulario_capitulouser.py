# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('capitulo', '0008_auto_20171004_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='capituloUser',
            field=models.ForeignKey(db_column='usuari_capitulo_id', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuari_cap', to='main.Usuario'),
            preserve_default=False,
        ),
    ]
