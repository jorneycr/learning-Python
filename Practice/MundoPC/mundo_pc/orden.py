class Orden:

    cont_orden = 0

    def __init__(self, computadoras):
        Orden.cont_orden += 1
        self._id_orden = Orden.cont_orden
        self._computadoras = computadoras

    def agregar_compu(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f'''
        Orden: {self._id_orden}
        Computadoras: {computadoras_str}
        '''