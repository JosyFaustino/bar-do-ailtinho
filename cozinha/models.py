from statistics import mode
from django.db import models
from django.forms import BooleanField
from django.urls import translate_url

# Create your models here.
class Product:
    CHOICES_TYPES = (
        (1, 'comidas'),
        (2, 'bebidas'),
        (3, 'sobremesas')
    )

    name = models.CharField(verbose_name='Nome do produto', max_length=100)
    type = models.IntegerField(verbose_name='Tipo do produto', choices=CHOICES_TYPES, null=True, blank=translate_url)
    value = models.CharField(verbose_name='Valor do produto')
    description = models.CharField(verbose_name='Descrição do produto', max_length=500)
    is_active = models.BooleanField(verbose_name='Está ativo?', default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.name

class Table:
    number = models.IntegerField(verbose_name='Número da mesa')
    seaters = models.IntegerField(verbose_name='Número de assentos')
    details = models.CharField(verbose_name='Detalhes da mesa')
    is_active = models.BooleanField(verbose_name='Está ativa?', default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
