from django import forms
from lojinha.models import Pedido

class PedidoCriarForm(forms.Modelform):
    class Meta:
        model = Pedido
        fields = [
            'nome',
            'email',
            'endereco',
            'observacao',
            'cartao',
            'pagamento'

        ]

        
