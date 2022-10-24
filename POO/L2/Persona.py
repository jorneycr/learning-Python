class Persona:
    def __init__(self,nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # permite que sea llamado como si fuera atricuto
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def motrarDetalle(self):
        print(f'{self._nombre} {self._apellido} {self._edad}')

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

if __name__ == '__main__':
    perso = Persona('Jorney','Lopez',27)
    perso.motrarDetalle()
    perso.nombre = 'Ismael'
    perso.apellido = 'Lopez Cordero'
    perso.edad = 'Un mes'
    perso.motrarDetalle()

    print(__name__)

