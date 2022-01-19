from produto import Produto


class CarrinhoDeCompras:

    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produto(self, produto: Produto) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        print('Compras Finalizadas!')

        for produto in self.__produtos:
            produto.informacoes_produto()

        self.__produtos = []