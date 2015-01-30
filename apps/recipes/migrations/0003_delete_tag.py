# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_comment_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
