# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list_shared_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='shared_with',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='shared_lists'),
        ),
    ]
