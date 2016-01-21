# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbtemplates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', verbose_name='sites', blank=True),
        ),
    ]
