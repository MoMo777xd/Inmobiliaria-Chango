# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alquiler',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
