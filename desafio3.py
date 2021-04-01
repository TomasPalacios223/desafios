""" devuelve si una letra ingresada por teclado es mayuscula o minuscula"""

letra = input("Ingrese una letra: ")

if letra >="a" and letra <="z":
    print("la letra ingresada es minuscula")
elif letra >="A" and letra <="Z":
    print("la letra ingresada es mayuscula")
else:
    print("lo ingresado no es una letra, por favor vuelva a intentarlo")