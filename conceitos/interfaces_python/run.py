from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangular import TerrenoRetangular
from engenheiro import Engenheiro


engenheiro = Engenheiro('Julio')

terreno_quadrado = TerrenoQuadrado(4)
terreno_retangular = TerrenoRetangular(2, 3)

engenheiro.medir_area(terreno_quadrado)
engenheiro.medir_area(terreno_retangular)

engenheiro.medir_perimetro(terreno_quadrado)