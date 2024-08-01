from Functions import *

while True:
    menu()
    opcao = int(input('Opção: '))
    print(' ')
    if opcao == 1:
        cadastrarClientes()
        while True:
            escolha = str(input('Quer continuar? [S/N]: ')).upper()
            if escolha == 'S':
                cadastrarClientes()
            elif escolha == 'N':
                break
    elif opcao == 2:
        escolha_2 = int(input('[1] - Lista de clientes  [2] - Lista de Reservas \n Opção: '))
        match escolha_2:
            case 1:
                #listarClientes()
            case 2:
                listarReservas()
            case _:
                print("Não há opção")
    elif opcao == 3:
        pesquisarCpfClientes()
    elif opcao == 4:
        editarCliente()
    elif opcao == 5:
        deletarClientes()
    elif opcao == 6:
        break