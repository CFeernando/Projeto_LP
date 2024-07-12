import Classes.Reserva

def cadastro():
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    contato = str(input('Contato: '))
    id = str(input('ID: '))
    novo = Classes.Reserva()
    novo.cadastro_cliente(nome, cpf, contato, id)

    for cliente in novo.hotel.lista_cadastro:
        print(cliente)

cadastro()