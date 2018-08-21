# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180821_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='archivo',
            field=models.ImageField(upload_to=b'documents/'),
        ),
    ]
