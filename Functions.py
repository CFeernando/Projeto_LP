from Classes.Hotel import *
import random

def menu():
    print('{0:^20}'.format('-' * 20))
    print('{0:^20}'.format('HOTEL PARADISE'))
    print('{0:^20}'.format('-' * 20))
    print(' ')
    print('[1] - Cadastar cliente \n[2] - Listagem \n[3] - Pesquisar \n[4] - Editar \n[5] - Excluir \n[6] - Sair')

def cadastro():
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    contato = str(input('Contato: '))
    id = str(*random.sample(range(1000, 5000), 1))
    global cliente
    cliente = Cliente(nome, cpf, contato,id)
    global add
    add = Reserva()
    add.fazer_cadastro_cliente(cliente)

def listarClientes():
    print('-'*80)
    if len(add.cadastro_cliente) > 0:
        for cliente in add.cadastro_cliente:
            print('{0:<15} {1:<20} {2:<25} {3:<30}'.format(cliente.nome, cliente.cpf, cliente.contato, cliente.id))
    else:
        print('Não há nada na base de dados.')

def listarReservas():
    global add_2
    add_2 = Hotel()
    print(add_2.listaReserva())

def pesquisaCpf():
    valorPesquisa = str(input('Digite o CPF: '))
    if len(add.cadastro_cliente) > 0:
        for cliente in add.cadastro_cliente:
            if cliente.cpf == valorPesquisa:
                print('Nome: ', cliente.nome)
                print('CPF: ', cliente.cpf)
                print('Contato: ', cliente.contato)
                print('ID: ', cliente.id)
            else:
                print('Cliente não encontrado.')
    else:
        print('Não há nada na base de dados.')

def editarCliente():
    pesquisaCpf()
    opcao = int(input('O que pretende editar? \n [1] - Nome  [2] - CPF  [3] - Contato \n'))
    match opcao:

        case 1:
            valor = input('Digite o novo nome: ')
            cliente.nome(valor)
            print('Nome: ', cliente.nome)
            print('CPF: ', cliente.cpf)
            print('Contato: ', cliente.contato)
            print('ID: ', cliente.id)

