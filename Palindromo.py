import os

def Limpiar(Cadena):
    CaracteresProhibidos = ['@', '+', '-', ' ', '¿', '?', '¡', '!', '[', ']', '.', ',', ':', ';', '/', '\\']
    Reemplazos = [
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u")
        ]
    
    # Eliminar los tildes
    for a, b in Reemplazos:
        Cadena = Cadena.replace(a, b).replace(a.upper(), b.upper())

    # Dejar toda la cadena en minusculas
    CadenaFinal = Cadena.lower()
    sep = ''

    # Eliminar caracteres prohibidos
    for i in CadenaFinal:
        if(i in CaracteresProhibidos):
            # En el caso de que haya un \n
            if(i == '\\' ):
                CadenaFinal = sep.join(CadenaFinal.split('\\n'))
            CadenaFinal = sep.join(CadenaFinal.split(i))
    return CadenaFinal 

def Palindromo(Cadena, Archivo):
    CadenaLimpia = Limpiar(Cadena)
    
    Archivo.write("Input limpio (sin caracteres prohibidos): " + CadenaLimpia + "\n")

    i = 0
    j = len(CadenaLimpia) - 1

    while(True):
        if(len(CadenaLimpia) == 0 or len(CadenaLimpia) == 1):
            print("No es palindromo")
            Archivo.write("Output: No es palindromo\n\n")
            return False
        elif(i >= j):
            print("Es palindromo")
            Archivo.write("Output: Es palindromo\n\n")
            return True
        elif(CadenaLimpia[i] != CadenaLimpia[j]):
            print("No es palindromo")
            Archivo.write("Output: No es palindromo\n\n")
            return False
        else:
            i = i + 1
            j = j - 1

file = open("./logs.txt", "w")
cont = 1

while(True):
    print("\n----------------------------------------------------------")
    print("| 1. Ingresar una cadena para verificar si es palindromo |")
    print("| 2. Salir                                               |")
    print("----------------------------------------------------------")
    print("Seleccione una opcion: ")
    opcion = input()

    if(opcion == '1'):
        print("Ingrese la cadena: ")
        ingreso = input()
        file.write("Caso de prueba " + str(cont) + "\n")
        file.write("Input: " + ingreso + "\n")
        Palindromo(ingreso, file)
        cont = cont + 1

    elif(opcion == '2'):
        break

    else:
        print("Opcion invalida, seleccione nuevamente")

file.close()