from Classes.Hotel import *
from Classes.Cliente import *

class Reserva:
    def __init__(self):
        self.hotel = Hotel
        self.cadastro_cliente = []  # Lista para armazenar clientes

    def fazer_cadastro_cliente(self, cliente):
        self.cliente = Cliente()
        self.cadastro_cliente.append(cliente)

    def lista_Cliente(self):
        return self.cadastro_cliente

