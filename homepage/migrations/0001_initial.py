# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-20 05:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_packages', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=50)),
                ('fecha', models.DateField(default='2018-03-20')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ciudad', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='homepage.City', verbose_name='Ciudad')),
                ('hours', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='homepage.Packages', verbose_name='Horas')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
