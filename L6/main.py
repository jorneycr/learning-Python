lista = ['Jorney', 'Ismael', "Daniel"]

def myFunction():
    for nombre in lista:
        if nombre == 'Ismael':
            print(f'El bebe nacido es: {nombre}')

myFunction()

def sayName(name,  edad):
    print(f'Nombre del bebe {name} y  edad del bebe {edad} mes')

sayName('Ismael',1)

def sumar(a,b):
    return a + b
res =  sumar(5,3);

print(res)

def listNames(*names):
    for name in names:
        print(name)

listNames('Jorney','Daniel', 'Lopez')

def listTerm(**term):
    for key, value in term.items():
        print(f'{key}:  {value}')

listTerm(JS='JavaScript',  TS='Typescript')


def desple(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Jorney','Dyrlen','Ismael']

desple(nombres)

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

res = factorial(4)
print(res)