"""dadas 2 cadenas de caracteres imprime la que mas caracteres tiene"""

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

if len(cadena1) > len(cadena2):
    print("se imprimira la cadena con mayor longitud")
    print()
    print(cadena1)
elif len(cadena1) < len(cadena2):
    print("se imprimira la cadena con mayor longitud")
    print()
    print(cadena2)
else:
    print("las dos cadenas ingresadas tienen igual longitud")