"""Ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir
aquellas que empiecen y terminen con la misma letra."""

palabra= input("ingrese una palabra el corte de control es fin ")
palabra=palabra.lower()
while palabra != "fin":
    cant=len(palabra)
    if((palabra[0])==(palabra [cant -1])):
        print(f'la palabra {palabra} empieza y termina con la misma letra')
    palabra= input("ingrese una palabra el corte de control es fin ")
    palabra=palabra.lower()
