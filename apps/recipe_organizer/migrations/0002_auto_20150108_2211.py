# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_organizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(help_text='This is a quick description of your recipe', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.TextField(help_text='How to make the recipe', default=''),
            preserve_default=False,
        ),
    ]
