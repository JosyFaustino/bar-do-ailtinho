# Generated by Django 4.0.4 on 2022-04-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozinha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='is_busy',
            field=models.BooleanField(default=False, verbose_name='Está ocupada?'),
        ),
    ]
