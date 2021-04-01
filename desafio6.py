"""el siguiente programa imprime la cant de letras a, que tiene una cadena de caracteres ingresada por teclado"""

cadena = input("Ingrese una cadena de caracteres : ")

cant = 0

cadena=cadena.lower()


for letra in cadena:
    if letra == "a":
        cant = cant + 1
print("la cadena ingresada tiene la siguiente cantidad de letras a : ")
print (cant)