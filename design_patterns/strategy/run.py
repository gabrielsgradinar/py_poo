from src import Guerreiro, LutaArco, LutaEspada, Curar

cavaleiro = Guerreiro(LutaEspada(6))
arqueiro = Guerreiro(LutaArco(10))

cavaleiro.acao()
arqueiro.acao()
arqueiro.atributos()