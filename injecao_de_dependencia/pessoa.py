

class Casa:
    
    def __init__(self) -> None:
        self.__endereco = "Rua Clevelância"

    def acender_luzes(self) -> None:
        print('Estou acendendo as luzes!')

    def get_endereco(self) -> str:
        return self.__endereco


class Pessoa:

    def __init__(self, nome, local: Casa) -> None:
        self.__local = local
        self.__nome = nome

    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)


casa_de_amigo = Casa()
julia = Pessoa('Julia', casa_de_amigo)


julia.entrar_no_local()
julia.apresentar_local()



