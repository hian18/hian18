from django.db import models
from datetime import datetime
from ..produtos.models import Produto


# Create your models here.

class ProdutoVenda(models.Model):
    quatidade = models.IntegerField(max_length=3)
    preco = models.FloatField()
    produto=models.ForeignKey(Produto,on_delete=models.CASCADE)


class Venda(models.Model):
    data_criacao = models.DateField(default=datetime.now(), editable=False)
    produtos_venda=models.ForeignKey(ProdutoVenda,on_delete=models.CASCADE)
    desconto=models.FloatField()

