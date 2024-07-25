from Functions import *

while True:
        opcao = int(input('Opção: '))
        print(' ')
        if opcao == 1:
            cadastro()
            while True:
                escolha = str(input('Quer continuar? [S/N]: ')).upper()
                if escolha=='S':
                    cadastro()
                elif escolha=='N':
                    break
        elif opcao == 2:
            listarClientes()
        elif opcao == 3:
            listarReservas()
        elif opcao == 4:
            pesquisaCpf()
        elif opcao == 5:
            break
