# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-28 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promanage', '0019_rentalapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalapplication',
            name='is_responded',
            field=models.BooleanField(default=False),
        ),
    ]
