"""Escribir un programa que ingrese 4 palabras desde el teclado e imprima aquellas que contienen la letra “r”."""

for i in range(4):
 cadena=input("ingrese una palabra:" )
 cadena=cadena.lower()
 mensaje= "Tiene r" if "r" in cadena else "la palabra no tiene r"
 print(mensaje)