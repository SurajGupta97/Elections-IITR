# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('branch', models.CharField(choices=[('CS', 'Computer Science'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering')], max_length=2, default='CS')),
                ('year', models.IntegerField(choices=[(1, 'First year'), (2, 'Second year'), (3, 'Third year'), (4, 'Fourth year')], default=1)),
                ('en_no', models.IntegerField()),
                ('post', models.BooleanField()),
            ],
        ),
    ]
