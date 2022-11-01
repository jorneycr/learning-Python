from mundo_pc.dispositivo_entrada import Dispositivo


class Raton(Dispositivo):

    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Id {self._id_raton}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada} \r\n'

if __name__ == '__main__':
    raton = Raton('HP','USB')
    raton1 = Raton('Acer','USB')

    print(raton, raton1)