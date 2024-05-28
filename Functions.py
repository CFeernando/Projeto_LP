from Classes import *


def cadastro():
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    contato = str(input('Contato: '))

    cliente = Reserva()
    cliente.cadastro_cliente(nome, cpf, contato)


cadastro()

