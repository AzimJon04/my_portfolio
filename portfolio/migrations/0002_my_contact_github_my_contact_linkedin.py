# Generated by Django 4.2.4 on 2023-08-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_contact',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='my_contact',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
    ]
