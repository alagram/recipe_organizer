# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='This is a quick description of your recipe', blank=True)),
                ('directions', models.TextField(help_text='How to make the recipe')),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
