from domain.Hotel import Hotel


class Reserva:
    _todas_reservas = []

    def __init__(self, cliente):
        hotel = Hotel()
        self._todas_reservas.append({cliente: hotel})



    @property
    def listaReserva(self):
        return self._todas_reservas

    @classmethod
    def find_all_reservas(cls):
        return cls._todas_reservas

    @classmethod
    def delete_reserva(cls, cpf):
        if len(cls._todas_reservas) > 0:
            for contador in cls._todas_reservas:

                for cliente, hotel in contador.items():
                    if cliente.cpf == cpf:
                        cls._todas_reservas.remove({cliente: hotel})
                        return 'Cliente removido com sucesso !'
                else:
                        return 'Cliente nao encontrado !'
        else:
            return 'Não há nada na base de dados.'