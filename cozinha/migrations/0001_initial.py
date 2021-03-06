# Generated by Django 4.0.3 on 2022-04-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome do produto')),
                ('type', models.IntegerField(choices=[(1, 'comidas'), (2, 'bebidas'), (3, 'sobremesas')], default=1, verbose_name='Tipo do produto')),
                ('value', models.CharField(max_length=8, verbose_name='Valor do produto')),
                ('description', models.CharField(max_length=500, verbose_name='Descrição do produto')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Número da mesa')),
                ('seaters', models.IntegerField(verbose_name='Número de assentos')),
                ('details', models.CharField(max_length=500, verbose_name='Detalhes da mesa')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativa?')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
