class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        if self.nombre == 'Ismael':
            return f'Persona: Nombre {self.nombre} Edad {self.edad} mes'
        else:
            return f'Persona: Nombre {self.nombre} Edad {self.edad} años'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'

# empleado1 = Empleado('Ismael', 27, 5000)
# print( f'{empleado1.nombre} {empleado1.edad} {empleado1.sueldo}')
