# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RookkaProject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RookkaProject.Result')),
            ],
        ),
        migrations.RemoveField(
            model_name='query',
            name='pub_date',
        ),
    ]