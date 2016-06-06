# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import Mail_blacklist.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128, null=True)),
                ('user_id', models.IntegerField(default=0)),
                ('type', Mail_blacklist.models.EnumField(choices=[('Bounce', 'Bounce'), ('Blacklist', 'Blacklist')], default='Bounce')),
            ],
            options={
                'db_table': 'blacklist',
            },
        ),
        migrations.AlterUniqueTogether(
            name='blacklist',
            unique_together=set([('email', 'user_id')]),
        ),
    ]
