from Hotel import Hotel
from Cliente import Cliente

class Reserva:
    def __init__(self):
        self.hotel = Hotel()
        self.cadastro_cliente = []  # Lista para armazenar clientes

    def fazer_cadastro_cliente(self, nome, cpf, contato, id):
        cliente = Cliente(nome, cpf, contato, id)
        self.cadastro_cliente.append(cliente)
        cadastro_hotel = {"CPF": cliente.cpf, "ID": cliente.id}
        self.hotel.listaReserva().append(cadastro_hotel)

# Criar instância de Reserva
# novo = Reserva()

# Fazer cadastro de cliente
#novo.fazer_cadastro_cliente("Samuel", 000, 111, 222)

# Imprimir os cadastros do hotel
#for cliente in novo.hotel.lista_cadastro:
    #print(cliente)