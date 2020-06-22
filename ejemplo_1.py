"""
Es un comentario 
"""
# Eso es otro comentario

name = ""
age = 8
soltero = True  # False

notas = [12, 14, 15, 12]
status = ('Activo', 'Inactivo', 'Cancelado')
opciones = {"Activo", "Inactivo"}

person = {
    "nombre": "Luis",
    "apellido": "Rodriguez",
    "edad": 38,
    "soltero": True
}

a = 7
b = 3
c = 6

if a > b and a > c:
    print(f"Mayor es a ({a})")
    print("Mayor es a (%s)" % a)
elif b > c: 
    print(f"Mayor es b ({b})")
    print("Mayor es b (%s)" % b)
elif c > a:
    print(f"Mayor es c ({c})")
    print("Mayor es c (%s)" % c)

# && , ||, !
# and or not
# + - / *
# ==, !=, >, <, >=, <=

""" nombre = "Luis"
apellido = "Rodriguez"
edad = "False"

nombre + apellido + bool(edad) """


""" if age > 18:
    print("Mayor de Edad")
else:
    print("Menor de Edad") """


for i in range(10, -1, -1): # (start=0, stop, step=1) 
    print(i)


for n in notas:
    print(n)

for i in range(len(notas)):
    print(notas[i])

for n in status:
    print(n)

for i in range(len(status)):
    print(status[i])


i = 1
while i <=10:
    print(i)
    i=i+1


def suma(a, b=6):
    return a + b
    a = b

def resultado():
    a = 8
    b = 10
    return suma(a, b)


resta = lambda a, b: a - b


print(resultado())
print(resta(4, 6))

user = {
    "username": "lparra"
}

username = user["username"] if user is not None else "anonimous"
print(username)