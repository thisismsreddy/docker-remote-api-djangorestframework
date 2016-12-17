# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('container_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('container_name', models.CharField(default=b'', max_length=100, blank=True)),
                ('container_image', models.CharField(default=b'', max_length=100, blank=True)),
                ('container_status', models.CharField(default=b'', max_length=100, blank=True)),
                ('container_ip', models.CharField(default=b'', max_length=100, blank=True)),
                ('container_port', models.CharField(default=b'', max_length=100, blank=True)),
                ('container_time', models.CharField(default=b'', max_length=100, blank=True)),
            ],
        ),
    ]
