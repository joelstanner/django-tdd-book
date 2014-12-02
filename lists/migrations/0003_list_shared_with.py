# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0002_list_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
