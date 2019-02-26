from django.contrib import admin
from lojinha.models import Produto, Pedidos, Pagamentos

admin.site.register(Produto)
admin.site.register(Pedidos)
admin.site.register(Pagamentos)