from Functions import *

while True:
    menu()
    opcao = int(input('Opção: '))
    print(' ')
    if opcao == 1:
        nome = str(input('Nome: '))
        cpf = str(input('CPF: '))
        contato = str(input('Contato: '))
        cadastrarClientes(nome, cpf, contato)
        while True:
            escolha = str(input('Quer continuar? [S/N]: ')).upper()
            if escolha == 'S':
                cadastrarClientes()
            elif escolha == 'N':
                break
    elif opcao == 2:
        listarReservas()

    elif opcao == 3:
        valor_cpf = str(input('Digite o CPF: '))
        print(pesquisarCpfClientes(valor_cpf))

    elif opcao == 4:
        valor_cpf = str(input('Digite seu CPF : \n'))
        print(editarClienteReserva(valor_cpf))

    # elif opcao == 5:
    #     # deletarClientes()

    elif opcao == 6:
        break