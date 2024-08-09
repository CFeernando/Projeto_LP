import random

class Cliente:
    def __init__(self, nome, cpf, contato):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.id = str(*random.sample(range(1000, 5000), 1))
    #Getter
    @property
    def nome(self):
        return self._nome
    
    #Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        self._cpf = valor

    @property
    def contato(self):
        return self._contato

    @contato.setter
    def contato(self, valor):
        self._contato = valor

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor


    def zerarCliente(self):
        self.nome = None
        self.cpf = None
        self.contato = None
        self.id = None

    def printarCliente(self):
        return (f"Nome: {self.nome} \nCPF: {self.cpf}"
                f"\nContato: {self.contato} \nID: {self.id}")