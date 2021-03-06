# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 08:35
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify


def forwards_func(apps, schema_editor):
    Card = apps.get_model('kanban', 'Card')
    db_alias = schema_editor.connection.alias
    for card in Card.objects.using(db_alias).all():
        card.slug = slugify(card.title, allow_unicode=True)
        card.save()


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0002_card_slug'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
