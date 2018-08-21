# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180821_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('property', models.ForeignKey(related_name='images', to='blog.Property')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='archivo',
            field=models.FileField(upload_to=b'documents/'),
        ),
    ]
