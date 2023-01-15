import math
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

while True:
    menu()
    opcion = int(input("Ingrese una opción: "))

    if opcion == 10:
        break

    else:
        num1 = float(input("Introduce tu primer número:"))
        num2 = float(input("Introduce tu segundo número:"))
        operaciones(num1, num2)

