from abc import ABC, abstractmethod

class Animal(ABC):
    _count = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Animal._count += 1

    @abstractmethod
    def emitir_som(self):
        pass

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    @classmethod
    def get_contador(cls):
        return cls._count

class Cachorro(Animal):
    def __init__(self, nome, idade, raça):
        super().__init__(nome, idade)
        self.raça = raça

    def emitir_som(self):
        return "Au Au"

    def get_raça(self):
        return self.raça

    def set_raça(self, raça):
        self.raça = raça

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def emitir_som(self):
        return "Miau Miau"

    def get_cor(self):
        return self.cor

    def set_cor(self, cor):
        self.cor = cor

if __name__ == "__main__":
    cachorro = Cachorro("Rex", 5, "Labrador")
    gato = Gato("Mingau", 3, "Preto")

    print(f"Cachorro: Nome = {cachorro.get_nome()}, Idade = {cachorro.idade}, Raça = {cachorro.get_raça()}")
    print(f"Som do cachorro: {cachorro.emitir_som()}")

    print(f"Gato: Nome = {gato.get_nome()}, Idade = {gato.idade}, Cor = {gato.get_cor()}")
    print(f"Som do gato: {gato.emitir_som()}")

    cachorro.set_nome("Max")
    gato.set_cor("Branco")

    print(f"Nome atualizado do cachorro: {cachorro.get_nome()}")
    print(f"Cor atualizada do gato: {gato.get_cor()}")

    print(f"Total de animais instanciados: {Animal.get_contador()}")

