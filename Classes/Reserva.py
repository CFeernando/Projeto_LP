from Classes.Cliente import *

class Reserva:
    def __init__(self):
        self.cadastro_cliente = []  # Lista para armazenar clientes

    def fazer_cadastro_cliente(self, cliente):
        self.cliente = Cliente(nome=None, cpf=None, contato=None, id=None)
        self.cadastro_cliente.append(cliente)

    def lista_Cliente(self):
        return self.cadastro_cliente

    def acessar_valor_da_instancia(self):
            return self.cadastro_cliente.cliente.cpf and self.cadastro_cliente.cliente.id

