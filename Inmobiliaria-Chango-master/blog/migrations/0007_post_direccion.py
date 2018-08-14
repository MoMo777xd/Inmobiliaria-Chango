# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_zona'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='direccion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
