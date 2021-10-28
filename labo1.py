#!/usr/bin/python3

try:
    letra=input("Ingrese una letra para formar la pirámide: ")
    altura=int(input("Ingrese la altura de la pirámide: "))
    altura_respaldo=altura -1
except ValueError:
    print("Alguno de los valores ingresados no coincide con el tipo de dato solicitado, intente nuevamente")
    exit()

while altura > 0:
    print(letra, end="")
    altura = altura -1
    if altura == 0:
        altura=altura_respaldo
        print("")
        altura_respaldo=altura_respaldo -1




