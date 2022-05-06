# Generated by Django 3.1.1 on 2020-09-29 01:27

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('patchwork', '0043_merge_patch_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='linkname',
            field=models.CharField(
                max_length=255,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile('^[-\\w]+\\Z'),
                        'Enter a valid “slug” consisting of Unicode '
                        + 'letters, numbers, underscores, or hyphens.',
                        'invalid',
                    )
                ],
            ),
        ),
    ]
