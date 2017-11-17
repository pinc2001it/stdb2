# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-17 10:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unittests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandpassanalysis',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bandpass_owned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='spectralanalysis',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spectral_owned', to=settings.AUTH_USER_MODEL),
        ),
    ]
