# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-14 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20170412_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='classificacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Classificacao'),
        ),
    ]