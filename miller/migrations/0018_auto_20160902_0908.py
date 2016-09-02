# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-02 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0017_story_covers'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='metadata',
            field=jsonfield.fields.JSONField(default=b'{"abstract": {"fr": "", "en": ""}, "title": {"fr": "", "en": ""}}'),
        ),
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[(b'bibtex', b'bibtex'), (b'video-cover', b'video interview'), (b'video', b'video'), (b'text', b'text'), (b'picture', b'picture'), (b'pdf', b'pdf'), (b'image', b'picture'), (b'photo', b'picture'), (b'rich', b'rich'), (b'link', b'link'), (b'audiovisual', b'audiovisual')], max_length=24),
        ),
    ]
