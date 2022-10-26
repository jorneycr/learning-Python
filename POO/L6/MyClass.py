class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodoEstatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodoClase(cls):
        print(cls.variable_clase)

MiClase.metodoEstatico()
MiClase.metodoClase()

print(MiClase.variable_clase)
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
