# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='git_url',
            field=models.URLField(default='www.nscp.dk'),
            preserve_default=False,
        ),
    ]
