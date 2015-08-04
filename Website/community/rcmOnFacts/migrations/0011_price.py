# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmOnFacts', '0010_auto_20150725_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipCode', models.CharField(default=b'#####', max_length=10)),
                ('money', models.IntegerField(default=b'0')),
            ],
        ),
    ]
