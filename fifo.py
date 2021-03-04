def capturar():
    global lista
    lista = []
    n = int(input("cual es el numero de procesos: "))
    for i in range(0, n):
        print("ingrese el nombre del proceso: ", i+1)
        elemento = input()
        lista.append(elemento)


def mostrar():
    print(lista)


def agregar():
    elemento = int(input("ingrese el proceso nuevo: "))
    lista.append()
    print("nuevo elemento agregado")


def terminar():
    lista.pop(0)
    print(lista)


def menu_principal():
    opcion = "1"
    while opcion != 5:
        print("digite el numero de  la accion a realizar: ")
        print("1: capturar")
        print("2: mostrar")
        print("3: agregar")
        print("4. eliminar")
        opcion = input()
        if opcion == "1":
            capturar()
        elif opcion == "2":
            mostrar()
        elif opcion == "3":
            agregar()
        elif opcion == "4":
            terminar()


menu_principal()
