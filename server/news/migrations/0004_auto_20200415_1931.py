# Generated by Django 3.0.5 on 2020-04-15 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200415_0832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='byline',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='versioncreated',
            new_name='datePublished',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='located',
            new_name='location',
        ),
    ]