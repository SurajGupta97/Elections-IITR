# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_auto_20151004_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('branch', models.CharField(max_length=2, default='CS', choices=[('CS', 'Computer Science'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering')])),
                ('year', models.IntegerField(default=1, choices=[(1, 'First year'), (2, 'Second year'), (3, 'Third year'), (4, 'Fourth year')])),
                ('gender', models.CharField(max_length=6, default='Male', choices=[('Male', 'Male'), ('Female', 'Female')])),
                ('dob', models.DateField()),
                ('en_no', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
