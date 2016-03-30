# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 09:38
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=32, unique=True)),
                ('category', models.CharField(default=b'keyword', max_length=32, validators=[django.core.validators.RegexValidator(b'^[0-9a-z-A-Z\\s]*$', b'Only 0-9 are allowed.', b'Invalid Number')])),
            ],
        ),
        migrations.AlterField(
            model_name='story',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='authors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='story',
            name='watchers',
            field=models.ManyToManyField(blank=True, related_name='watchers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(blank=True, to='miller.Tag'),
        ),
    ]
