# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(max_length=75, serialize=False, primary_key=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_query_name='user', blank=True, to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_name='user_set', help_text='Specific permissions for this user.', related_query_name='user', blank=True, to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
