# condiccion = 'hello'
#
# if condiccion == True:
#     print('es verdadero')
# elif condiccion == False:
#     print('es falso')
# else:
#     print('no corresponde')
#
# num = int(input('Valor entre 1 y 3 : '))
#
# numTex = ''
# if num == 1:
#     numTex = 'uno'
# elif num == 2:
#     numTex = 'dos'
# elif num == 3:
#     numTex = 'tres'
# else:
#     numTex = 'fuera de rango'
#
# print(f'Numero: {numTex}')

#ternario
condi = True
print('Condicion verdadera') if condi else print('condicion false')

mes = int(input('Mes del año (1-12) :'))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'primavera'
else:
    estacion = 'verano'

print(f'La estacion es {estacion}')