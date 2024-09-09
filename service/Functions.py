from domain.Cliente import Cliente
from domain.Reserva import Reserva


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
    cliente = Cliente(nome, cpf, contato)

    cliente.lista_clientes.append(cliente)

    newReserve = Reserva(cliente)


def listarReservas():
    print('-'*80)
    reservas = Reserva.find_all_reservas()
    if len(reservas) > 0:
        for contador in reservas:
            for cliente, hotel in contador.items():
                print(f'Cliente: {cliente.nome} CPF: {cliente.cpf} Contato: {cliente.contato}')
                print(f'Hotel: {hotel.nome}')
                print('-' * 80)
    else:
        print('Não há nada na base de dados.')

def buscarReservaPorCpf(cpf):
    reservas = Reserva.find_all_reservas()
    if len(reservas) > 0:
        for contador in reservas:
            for cliente, hotel in contador.items():
                if cliente.cpf == cpf:
                    return cliente.printarCliente()
                else:
                    return 'Cliente nao encontrado !'
    else:
        return 'Não há nada na base de dados.'


def editarClienteReserva(valor_cpf):

    clienteFound = buscarReservaPorCpf(valor_cpf)
    if(clienteFound == 'Cliente nao encontrado !' or clienteFound == 'Não há nada na base de dados.'):
        return 'Cliente nao encontrado !'
    
    opcao = int(input('O que pretende editar? \n [1] - Nome  [2] - CPF  [3] - Contato \n'))
    reservas = Reserva.find_all_reservas()
    for contador in reservas:
            for cliente, hotel in contador.items():
                if(opcao == 1):
                    nome = input('Digite o novo nome: ')
                    cliente.nome = nome
                    return cliente.printarCliente()
                
                elif(opcao == 2):
                    cpf = input('Digite o novo cpf: ')
                    cliente.nome = cpf
                    return cliente.printarCliente()
                
                elif(opcao == 3):
                    contato = input('Digite o novo contato: ')
                    cliente.nome = contato
                    return cliente.printarCliente()
                else:
                    return 'Erro ao atualizar ...'

def deletarReserva(cpf):
    return Reserva.delete_reserva(cpf)



