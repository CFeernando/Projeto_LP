from Classes.Reserva import *

class Hotel:
    def __init__(self):
        self.nome = "Hotel Paradise"
        self.cnpj = "77.537.261/0001-00"
        self.contato = "hotelparadise@gmail.com"

    def listaReserva(self):
        self.lista_Reserva = {}
        self.adiciona_Reserva = Reserva
        for cliente in self.adiciona_Reserva.lista_Cliente(self):
            for i in self.adiciona_Reserva.acessar_valor_da_instancia(cliente):
                print(i)
'''            cadastro_hotel = {'ID': adiciona_Reserva., 'CPF': adiciona_Reserva.cliente.cpf}.copy()
            self.lista_Reserva['ID'] = cadastro_hotel
        print('-' * 80)
        print('LISTA DE RESERVAS')
        print('-'*80)
        if len(self.lista_Reserva > 0):
            for cadastro_hotel in self.lista_Reserva:
                print('{0:<15} {1:<20}'.format(cadastro_hotel['CPF'], cadastro_hotel['ID']))'''
