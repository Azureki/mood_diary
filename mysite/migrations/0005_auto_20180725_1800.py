# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-25 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20180725_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='person_page',
            field=models.URLField(null=True),
        ),
    ]
