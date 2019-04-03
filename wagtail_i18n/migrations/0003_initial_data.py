# Generated by Django 2.1.7 on 2019-03-25 17:34

from django.conf import settings
from django.db import migrations

from wagtail_i18n.compat import get_supported_language_variant


def initial_data(apps, schema_editor):
    Language = apps.get_model('wagtail_i18n.Language')
    Region = apps.get_model('wagtail_i18n.Region')

    default_language, created = Language.objects.get_or_create(
        code=get_supported_language_variant(settings.LANGUAGE_CODE),
    )

    default_region = Region.objects.create(
        name='Default',
        slug='default',
    )

    default_region.languages.add(default_language)


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_i18n', '0002_region'),
    ]

    operations = [
        migrations.RunPython(initial_data, migrations.RunPython.noop)
    ]
