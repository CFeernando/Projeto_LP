from Hotel import Hotel
import Reserva

class Cliente:
    def __init__(self, nome, cpf, contato, id):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.id = id

    def __set__(self, instance, value):