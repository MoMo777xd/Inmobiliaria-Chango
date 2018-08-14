# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_antiguedad'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='servicios',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
