from Classes.Reserva import *

class Hotel:
    def __init__(self):
        self.nome = "Hotel Paradise"
        self.cnpj = "77.537.261/0001-00"
        self.contato = "hotelparadise@gmail.com"

    def listaReserva(self):
        lista_Reserva = {}
        adiciona_Reserva = Reserva()
        for cliente in adiciona_Reserva.lista_Cliente():
            cadastro_hotel = {'CPF': cliente.cpf, 'ID': cliente.id}.copy()
            lista_Reserva['ID'] = cadastro_hotel
            print('-' * 80)
            print('LISTA DE RESERVAS')
            print('-'*80)
            for cadastro_hotel in lista_Reserva:
                print('{0:<15} {1:<20}'.format(cadastro_hotel['CPF'], cadastro_hotel['ID']))
