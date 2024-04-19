from rest_framework import serializers
from app.models import Verduras, Frutas, Entrega, Pagamento, Item

class VerdurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verduras
        fields = ['nome', 'preco', 'estoque']

class FrutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frutas
        fields = ['nome', 'preco', 'qntdisponivel']

class EntregaSerializer(serializers.ModelSerializer):
    itens = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    pagamento = serializers.PrimaryKeyRelatedField(queryset=Pagamento.objects.all())

    class Meta:
        model = Entrega
        fields = ['nomeCliente', 'enderecoEntrega', 'dataDeEntrega', 'itens', 'pagamento']

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['FormasDePagamento', 'valorTotal']

class ItemSerializer(serializers.ModelSerializer):
    entrega = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())

    class Meta:
        model = Item
        fields = ['numeroItem', 'quantidade', 'precoUnitario', 'entrega']
