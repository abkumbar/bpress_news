# Generated by Django 3.0.5 on 2020-04-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('headline', models.CharField(max_length=2000)),
                ('author', models.CharField(max_length=200)),
                ('date_published', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Main article text')),
            ],
        ),
    ]
