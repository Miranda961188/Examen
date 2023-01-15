import math
import numpy as np
def menu():
    print(
        "Dime, ¿qué operación quieres hacer? \n 1) Suma \n 2) Resta \n 3) Multiplicar \n 4) Dividir \n 5) Exponente \n 6) Raiz cuadrada \n 7) Seno  \n 8) Coseno \n 9) Tangente \n10) Apagar calculadora \n")

def operaciones(numero1, numero2):
    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de", numero1, "+", numero2, "es igual a", numero1 + numero2, "\n")
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de", numero1, "-", numero2, "es igual a", numero1 - numero2, "\n")
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de", numero1, "*", numero2, "es igual a", numero1 * numero2, "\n")

    elif opcion == 4:
        print(" ")
        print("RESULTADO: El producto de", numero1, "/", numero2, "es igual a", numero1 / numero2, "\n")

    elif opcion == 5:
        print(" ")
        print("RESULTADO: Base", numero1, "exponente", numero2, "es igual a", numero1 ** numero2, "\n")
    else:
        print("Opcion incorrecta")
def operacion(numero1):
    if opcion == 6:
        print(" ")
        print("RESULTADO: La raiz cuadrada de", numero1, "es igual a", math.sqrt(numero1), "\n")
    elif opcion == 7:
        print(" ")
        print("RESULTADO: la operacion Seno de", numero1, "es igual a", np.sin(numero1), "\n")
    elif opcion == 8:
        print(" ")
        print("RESULTADO: la operacion Coseo de", numero1, "es igual a", np.cos(numero1), "\n")
    elif opcion == 9:
        print(" ")
        print("RESULTADO: la operacion Tangente de", numero1, "es igual a", np.tan(numero1), "\n")
    else:
        print("Opción incorrecta")

while True:
    menu()
    opcion = input("Ingrese una opción: ")

    if opcion.isnumeric():
        opcion = int(opcion)
        if opcion == 10:
            print("¡Hasta pronto! :)")
            exit(0)
        elif opcion == 5:
            num1 = float(input("Introduce el numero como base:"))
            num2 = float(input("Introduce el numero para exponente:"))
            operaciones(num1, num2)
        elif opcion == 6 or opcion == 7 or opcion == 8 or opcion == 9:
            num1 = float(input("Introduce el número: "))
            operacion(num1)
        elif opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
            num1 = float(input("Introduce tu primer número:"))
            num2 = float(input("Introduce tu segundo número:"))
            operaciones(num1, num2)
        else:
            print("Por favor ingrasa una opcion de la lista")
    else:
        print("Por favor ingrasa una opcion de la lista")