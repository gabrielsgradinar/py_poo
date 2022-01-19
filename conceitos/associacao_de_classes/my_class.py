class Interruptor:

    def __init__(self, comodo) -> None:
        self.__comodo = comodo

    
    def acender(self):
        print(f'Acendendo {self.__comodo}')

    def apagar(self):
        print(f'Apagando {self.__comodo}')



class Pessoa:

    def acender_luz(self, interruptor: Interruptor):
        interruptor.acender()

    def apagar_lux(self, interruptor: Interruptor):
        interruptor.apagar()

    
    def dormir(self):
        print("Fui domir zzz")



gabriel = Pessoa()
interruptor_quarto = Interruptor('Quarto')
interruptor_cozinha = Interruptor('Cozinha')


gabriel.acender_luz(interruptor_quarto)
gabriel.apagar_lux(interruptor_quarto)
gabriel.apagar_lux(interruptor_cozinha)
gabriel.dormir()