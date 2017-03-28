# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chedule', '0007_auto_20170328_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchedule',
            name='friday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday', to='chedule.DayChedule', verbose_name='Пятница'),
        ),
        migrations.AlterField(
            model_name='groupchedule',
            name='monday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday', to='chedule.DayChedule', verbose_name='Понедельник'),
        ),
        migrations.AlterField(
            model_name='groupchedule',
            name='saturday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday', to='chedule.DayChedule', verbose_name='Суббота'),
        ),
        migrations.AlterField(
            model_name='groupchedule',
            name='thursday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday', to='chedule.DayChedule', verbose_name='Четверг'),
        ),
        migrations.AlterField(
            model_name='groupchedule',
            name='tuesday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday', to='chedule.DayChedule', verbose_name='Вторник'),
        ),
        migrations.AlterField(
            model_name='groupchedule',
            name='wednesday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday', to='chedule.DayChedule', verbose_name='Среда'),
        ),
    ]