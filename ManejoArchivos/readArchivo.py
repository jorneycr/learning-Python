def app():
    with open('archivo.txt') as archivo:
        for cont in archivo:
            print(cont.rstrip())

app()