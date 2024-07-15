from Classes.Reserva import *

class Hotel:
    def __init__(self):
        self.nome = "Hotel Paradise"
        self.cnpj = "77.537.261/0001-00"
        self.contato = "hotelparadise@gmail.com"

    @staticmethod
    def listaReserva():
        adiciona_Reserva = Reserva.lista_Cliente()
        lista_cadastro = []

