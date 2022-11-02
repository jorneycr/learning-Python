from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Computadora:
    conta_pc = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.conta_pc += 1
        self._id_pc = Computadora.conta_pc
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_pc}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

if __name__ == '__main__':
    monitor = Monitor('HP', 15)
    teclado = Teclado('MSI', 'Tipo C')
    raton = Raton('Dell','USB')

    compu = Computadora('HP', monitor, teclado, raton)
    print(compu)

    monitor1 = Monitor('ACER', 15)
    teclado1 = Teclado('MSI', 'Tipo C')
    raton1 = Raton('Apple', 'USB')

    compu1 = Computadora('ACER', monitor1, teclado1, raton1)
    print(compu1)