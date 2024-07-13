from Classes import Reserva
from Classes import Cliente
def cadastro():
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    contato = str(input('Contato: '))
    id = str(input('ID: '))
    cliente = Cliente(nome, cpf, contato,id)

    #for cliente in novo.hotel.listaReserva():
        #print(cliente)

cadastro()