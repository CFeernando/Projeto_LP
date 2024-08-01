from Classes.Cliente import *
from Classes.Hotel import *

class Reserva:
    reservaCliente = []

    def fazerReserva(self, cliente:Cliente):
        hotel = Hotel()
        self.reservaCliente.append({cliente:hotel})

    @property
    def reservaCliente(self):
        return self._reservaCliente

    @classmethod
    def retornar_cadastro_cliente(cls):
        return cls.reservaCliente