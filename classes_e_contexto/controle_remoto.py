class ControleRemoto:
    
    def __init__(self, televisao, comodo) -> None:
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print("Canal Avancado")

    def voltar_canal(self):
        print('Voltar o canal')

    def escolher_canal(self, canal: int):
        print(f'Alterado para o canal: {canal}')


controle_sala = ControleRemoto('LG', 'sala')

print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal
controle_sala.escolher_canal(12)