from Classes.Reserva import *
import random

def menu():
    print('{0:^20}'.format('-' * 20))
    print('{0:^20}'.format('HOTEL PARADISE'))
    print('{0:^20}'.format('-' * 20))
    print(' ')
    print('[1] - Cadastar cliente \n[2] - Listagem \n[3] - Pesquisar \n[4] - Editar \n[5] - Excluir \n[6] - Sair')

def cadastrarClientes():
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    contato = str(input('Contato: '))
    #global cliente
    cliente = Cliente(nome, cpf, contato)
    #global reserva
    reserva = Reserva()
    reserva.fazerReserva(cliente)

'''def listarClientes():
    print('-'*80)
    if len(fazerReserva.cadastro_cliente) > 0:
        for cliente in cadastrarClientes():
            print('{0:<15} {1:<20} {2:<25} {3:<30}'.format(cliente.nome, cliente.cpf, cliente.contato, cliente.id))
    else:
        print('Não há nada na base de dados.')'''

def listarReservas():
    reservaHotel = Hotel()
    print(reservaHotel.listaReserva())

def pesquisarCpfClientes():
    valorPesquisa = str(input('Digite o CPF: '))
    if len(reserva.cadastro_cliente) > 0:
        for cliente in reserva.cadastro_cliente:
            if cliente.cpf == valorPesquisa:
                print(cliente.printarCliente())
            else:
                print('Cliente não encontrado.')
    else:
        print('Não há nada na base de dados.')

def editarCliente():
    pesquisarCpfClientes()
    opcao = int(input('O que pretende editar? \n [1] - Nome  [2] - CPF  [3] - Contato \n'))
    match opcao:

        case 1:
            valor = input('Digite o novo nome: ')
            cliente.nome = valor
            print(cliente.printarCliente())

        case 2:
            valor = input('Digite o novo CPF: ')
            cliente.cpf = valor
            print(cliente.printarCliente())

        case 3:
            valor = input('Digite o novo contato: ')
            cliente.contato = valor
            print(cliente.printarCliente())

        case default:
            return print('Error!')

def deletarClientes():
    valorPesquisa = str(input('Digite o CPF: '))
    if len(reserva.cadastro_cliente) > 0:
        for cliente in reserva.cadastro_cliente:
            if cliente.cpf == valorPesquisa:
                print('Nome: ', cliente.nome)
                print('CPF: ', cliente.cpf)
                print('Contato: ', cliente.contato)
                print('ID: ', cliente.id)
                reserva.cadastro_cliente.pop(cliente)
                print(' ')
                print('Cliente deletado!')
            else:
                print('Cliente não encontrado.')
    else:
        print('Não há nada na base de dados.')


