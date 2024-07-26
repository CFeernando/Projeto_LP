from Classes.Reserva import *

class Hotel:
    def __init__(self):
        self.nome = "Hotel Paradise"
        self.cnpj = "77.537.261/0001-00"
        self.contato = "hotelparadise@gmail.com"

    @staticmethod
    def listaReserva():
        lista_Reserva = {}
        adiciona_Reserva = Reserva()
        for cliente in adiciona_Reserva.cadastro_cliente:
            cadastro_hotel = {'CPF': cliente.cpf, 'ID': cliente.id}.copy()
            lista_Reserva[cliente.cpf] = cadastro_hotel
        print('-' * 80)
        print('LISTA DE RESERVAS')
        print('-' * 80)
        if len(lista_Reserva) > 0:
            for cadastro_hotel in lista_Reserva.values():
                print('{0:<15} {1:<20}'.format(cadastro_hotel['CPF'], cadastro_hotel['ID']))
