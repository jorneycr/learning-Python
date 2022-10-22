nombres = ["Jorney","Ismael","Daniel","Dyrlen"]

#imprir
print(nombres)

print(nombres[-1])
print(nombres[0:2])
print(nombres[:3])
print(nombres[2:])
nombres[2] = "Iveth"
print(nombres)

print(len(nombres))


for nombre in nombres:
    # print(nombre)
    print(nombre, end=' -> ')

for nombre in nombres:
    if nombre == "Ismael":
        print(f'Nacio: {nombre}')


nombres.append('Lopez')
print(nombres)
nombres.insert(1,"Oscar")
print(nombres)
nombres.remove("Oscar")
print(nombres)
nombres.pop()
print(nombres)
nombres.clear()
print(nombres)
# del nombres
# print(nombres)

# Dict

dic = {
    'title' : 'Unica mirando al mar',
    'año' : 2022,
    'realese' : 2000
}

print(dic)
print(dic['año'])
print(len(dic))
