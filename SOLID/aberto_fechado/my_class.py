class Circo:

    def apresentar(self, apresentador):
        apresentador.apresentar_show()

class Malabarista:

    def apresentar_show(self):
        print("Malabarista apresentando seu show")

class Palhaço:

    def apresentar_show(self):
        print("Palhaço apresentando seu show")


circo = Circo()

malabarista = Malabarista()
palhaco = Palhaço()

circo.apresentar(palhaco)
circo.apresentar(malabarista)