from Classes.Cliente import *

class Reserva:
    def __init__(self):
        self.cadastro_cliente = []  # Lista para armazenar clientes

    def fazer_cadastro_cliente(self, cliente):
        cliente = Cliente(nome='', cpf='', contato='', id='')
        self.cadastro_cliente.append(cliente)

    def lista_Cliente(self):
        return self.cadastro_cliente

