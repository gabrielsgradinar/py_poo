from abc import ABC, abstractclassmethod

class AbstractClass(ABC):

    @abstractclassmethod
    def metodo_abstrato(self) -> None:
        ...