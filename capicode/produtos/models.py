from django.db import models
from datetime import datetime
# Create your models here.

class Produto(models.Model):

    nome=models.CharField(max_length=100)
    descricao=models.CharField(max_length=200)
    preco=models.FloatField()
    data_criacao = models.DateField(default=datetime.now(),editable=False)
    thumbs=models.CharField(max_length=200)
    thumb_principal=models.CharField(max_length=200)
    fotos=models.CharField(max_length=200)
    foto_principal=models.CharField(max_length=50)

