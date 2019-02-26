from django.shortcuts import render
from loja.forms import PedidoCriarform

# Create your views here.

def criar_pedidoview(request):
    formulario = PedidoCriarform()

    contexto =[
        form: formulario

    ]

    return render (request, 'formulario-pedido.html', contexto)