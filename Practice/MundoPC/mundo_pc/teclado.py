from mundo_pc.dispositivo_entrada import Dispositivo


class Teclado(Dispositivo):

    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados = += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Id: {self._id_teclado}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'