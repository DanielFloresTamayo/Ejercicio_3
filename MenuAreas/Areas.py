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

def area_cuadrado():
    L = int(input('Ingrese el lado: '))
    area = L ** 2
    return print('El area del cuadrado es: ', area)

def AreaTriangulo():
    b = int(input('Ingrese la base: '))
    h = int(input('Ingrese la altura: '))
    area = b * h / 2
    return print('El area del triangulo es: ', area)



if n == 1:
    area_cuadrado()

if n==3:
    AreaTriangulo();

