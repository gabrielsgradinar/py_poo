class Produto:

    def __init__(self, prod_name: str, prod_valor: int) -> None:
        self.__prod_name = prod_name
        self.__prod_valor = prod_valor

    def informacoes_produto(self) -> None:
        print(f'Produto: {self.__prod_name} / valor: R$ {self.__prod_valor},00')

    