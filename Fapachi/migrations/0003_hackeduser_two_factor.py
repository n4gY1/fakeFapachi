# Generated by Django 4.0.1 on 2023-01-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fapachi', '0002_hackeduser_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackeduser',
            name='two_factor',
            field=models.BooleanField(default=False),
        ),
    ]
