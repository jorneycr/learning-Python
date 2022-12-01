import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='postgres',
    host='localhost',
    port='5438',
    dbname='postgres'
)
print(conexion)

cursor = conexion.cursor()
