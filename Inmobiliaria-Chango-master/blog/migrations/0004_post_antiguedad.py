# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180807_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='antiguedad',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
