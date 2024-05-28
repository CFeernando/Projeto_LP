class Reserva:   
    class Cliente:
        def __init__(self, nome, cpf, contato, id):
            self.nome = nome
            self.cpf = cpf
            self.contato = contato
            self.id = id

    class Hotel:
        def __init__(self):
            self.nome = "Hotel Paradise"
            self.cnpj = "77537261000"
            self.contato = "hotelparadise@gmail.com"
            self.lista_cadastro = []

    def __init__(self):
        self.hotel = self.Hotel()
        self.cadastro_cliente = []  # Lista para armazenar clientes
    
    def fazer_cadastro_cliente(self, nome, cpf, contato, id):
        cliente = self.Cliente(nome, cpf, contato, id)
        self.cadastro_cliente.append(cliente)
        cadastro_hotel = {"cpf": cliente.cpf, "id": cliente.id}
        self.hotel.lista_cadastro.append(cadastro_hotel)

# Criar instância de Reserva
novo = Reserva()

# Fazer cadastro de cliente
novo.fazer_cadastro_cliente("Samuel", 000, 111, 222)

# Imprimir os cadastros do hotel
for cliente in novo.hotel.lista_cadastro:
    print(cliente)  
