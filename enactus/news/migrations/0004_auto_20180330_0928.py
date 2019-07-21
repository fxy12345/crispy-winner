# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-30 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180319_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='kind',
            field=models.CharField(choices=[('技术', '技术'), ('新闻', '新闻'), ('财务', '财务'), ('人力', '人力'), ('公关', '公关'), ('团队', '团队')], default=('技术', '技术'), max_length=20),
        ),
    ]