# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-07 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthworker', '0002_permanentworker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permanentworker',
            name='user',
        ),
        migrations.AddField(
            model_name='healthworker',
            name='education_level',
            field=models.CharField(choices=[('Degree', 'Degree'), ('Diploma', 'Diploma'), ('Certificate', 'Certificate')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='healthworker',
            name='employment_type',
            field=models.CharField(choices=[('Permanent', 'Permanent'), ('Contract', 'Contract')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='healthworker',
            name='terminated_employee',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthworker',
            name='end_of_contract',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='PermanentWorker',
        ),
    ]
