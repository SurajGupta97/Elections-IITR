# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post', models.IntegerField()),
                ('votes', models.IntegerField(default=0)),
                ('manifesto', models.FileField(upload_to=b'/home/pdh1596/projects/Personal/Elections_IITR<django.db.models.fields.related.OneToOneField>')),
                ('image', models.ImageField(upload_to=b'/home/pdh1596/projects/Personal/Elections_IITR<django.db.models.fields.related.OneToOneField>')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
