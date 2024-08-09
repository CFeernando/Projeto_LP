from src.domain.Cliente import Cliente
from src.domain.Reserva import Reserva


def menu():
    print('{0:^20}'.format('-' * 20))
    print('{0:^20}'.format('HOTEL PARADISE'))
    print('{0:^20}'.format('-' * 20))
    print(' ')
    print('[1] - Cadastar cliente \n[2] - Listagem \n[3] - Pesquisar \n[4] - Editar \n[5] - Excluir \n[6] - Sair')


def cadastrarClientes(nome, cpf, contato):
    
    cliente = Cliente(nome, cpf, contato)
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

def pesquisarCpfClientes(cpf):
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

    clienteFound = pesquisarCpfClientes(valor_cpf) 
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

# def deletarClientes():
#     valorPesquisa = str(input('Digite o CPF: '))
#     if len(reserva.cadastro_cliente) > 0:
#         for cliente in reserva.cadastro_cliente:
#             if cliente.cpf == valorPesquisa:
#                 print('Nome: ', cliente.nome)
#                 print('CPF: ', cliente.cpf)
#                 print('Contato: ', cliente.contato)
#                 print('ID: ', cliente.id)
#                 reserva.cadastro_cliente.pop(cliente)
#                 print(' ')
#                 print('Cliente deletado!')
#             else:
#                 print('Cliente não encontrado.')
#     else:
#         print('Não há nada na base de dados.')


