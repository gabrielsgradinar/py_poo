from produto import Produto
from carrinho import CarrinhoDeCompras


carrinho = CarrinhoDeCompras()

monitor = Produto('Monitor', 1000)
mouse = Produto('Mouse', 100)

carrinho.adicionar_produto(monitor)
carrinho.adicionar_produto(mouse)

carrinho.finalizar_compra()