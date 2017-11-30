print("\tESCUELA POLITECNICA NACIONAL")
print("\t    EJERCICIO 3")
print("Integrantes: \n")
print("Daniel Flores\n")
print("Omar Diaz\n")
print("Jefferson Llumiquinga\n")

print ("1. Cuadrado\n")
print ("2. Círculo\n")
print ("3. Triángulo\n")
n = int(input("Ingrese la opción: "))

def areaCuadrado():
    L = int(input('Ingrese el lado: '))
    area = L ** 2
    return print('El area del cuadrado es: ', area)

def AreaTriangulo():
    b = int(input('Ingrese la base: '))
    h = int(input('Ingrese la altura: '))
    area = b * h / 2
    return print('El area del triangulo es: ', area)

def areaCirculo():
    rad = int(input("Ingrese el area del circulo: "))
    pi=3.14
    area =pi*(rad**2)

    return print("El Area del circulo es: ", area)

if n == 1:
    areaCuadrado()

if n == 2:
    areaCirculo()

if n==3:
    AreaTriangulo();

