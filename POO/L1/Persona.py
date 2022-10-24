class Persona:
    def __init__(self,nombre, apellido, edad, *valores, **terminos):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def motrarDetalle(self):
        print(f'{self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


perso = Persona('Jorney','Lopez',27, '65664', 10 , 10 , m='manzana', p='per')
perso.motrarDetalle()

perso1 = Persona('Ismael','Lopez',0)
Persona.motrarDetalle(perso1)
