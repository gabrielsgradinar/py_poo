from models import Elevador
from controller import GerenciadorDeElevadores

elevador1 = Elevador(1)
elevador2 = Elevador(2)

gerenciador_de_elevadores = GerenciadorDeElevadores(elevador1, elevador2)

while(True):
    elevadorId = int(input('Defina o elevador: '))
    andar = int(input('Defina um andar: '))

    resposta = gerenciador_de_elevadores.locomover(andar, elevadorId)

    print(resposta)
    print()