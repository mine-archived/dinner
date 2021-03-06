# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0001_initial'),
        ('public', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='calendar',
            field=models.ForeignKey(to='public.Calendar'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(to='dinner.MenuItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='calendar',
            field=models.ForeignKey(to='public.Calendar'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='provider',
            field=models.ForeignKey(verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86', to='public.Org', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendarprovider',
            name='calendar',
            field=models.ForeignKey(to='public.Calendar'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calendarprovider',
            name='provider',
            field=models.ForeignKey(to='public.Org'),
            preserve_default=True,
        ),
    ]
