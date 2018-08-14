# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_servicios'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='zona',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
