from django.db import models

class Verduras(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()

class Frutas(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qntdisponivel = models.IntegerField()

class Entrega(models.Model):
    nomeCliente = models.CharField(max_length=255)
    enderecoEntrega= models.TextField()
    dataDeEntrega = models.DateTimeField()
    pagamento = models.OneToOneField('Pagamento', on_delete=models.CASCADE, related_name='entrega')

class Pagamento(models.Model):
    mtPgto = models.CharField(max_length=50)
    vlrTotal = models.DecimalField(max_digits=8, decimal_places=2)

class Item(models.Model):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    numeroItem = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    precoUnitario = models.DecimalField(max_digits=6, decimal_places=2)
