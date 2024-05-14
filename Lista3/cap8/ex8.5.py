class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("Miau miau")

animal = Animal("Lua", 2)

animal.emitir_som()