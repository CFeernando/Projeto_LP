from Classes.Hotel import *

def cadastro():
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    contato = str(input('Contato: '))
    id = str(input('ID: '))
    global cliente
    cliente = Cliente(nome, cpf, contato,id)
    global add
    add = Reserva()
    add.fazer_cadastro_cliente(cliente)

def listarClientes():
    print('-'*80)
    for cliente in add.lista_Cliente():
        print('{0:<15} {1:<20} {2:<25} {3:<30}'.format(cliente.nome, cliente.cpf, cliente.contato, cliente.id))


def listarReservas():
    global add_2
    add_2 = Hotel()
    print(add_2.listaReserva())


cadastro()
listarClientes()
listarReservas()