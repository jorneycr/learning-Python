cont = 0

while cont < 3:
    print(cont)
    cont += 1
else:
    print('End while')

cadena = 'Hola'

for letra in cadena:
    print(letra)
else:
    print('End For')

for letre in 'Holanda':
    if letre == 'a':
        print(f'Letra encontrada: {letre}')
        break
else:
    print('End For')

for i in  range(6):
    # print(f'Valor: {i}')
    if i % 2 == 0:
        print(f'Par: {i}')