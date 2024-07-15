from Classes.Reserva import *
from Classes.Cliente import *
from Classes.Hotel import *

def cadastro():
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    contato = str(input('Contato: '))
    id = str(input('ID: '))
    cliente = Cliente(nome, cpf, contato,id)
    novo = Reserva()
    novo.fazer_cadastro_cliente(cliente)

    for cliente in novo.hotel.listaReserva():
        print(cliente)

cadastro()