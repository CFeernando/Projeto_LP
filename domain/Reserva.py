from domain.Cliente import *
from domain.Hotel import *

class Reserva:
    _todas_reservas = []

    def __init__(self, cliente):
        hotel = Hotel()
        self._todas_reservas.append({cliente: hotel})


    @property
    def listaReserva(self):
        return self._todas_reservas

    @classmethod
    def find_all_reservas(cls):
        return cls._todas_reservas
    