# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-16 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0018_auto_20170615_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ultima_msg_excluida',
            field=models.IntegerField(default=0),
        ),
    ]