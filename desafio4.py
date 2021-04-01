''' el siguiente programa imprime si un caracter ingresado por teclado es una comilla o no''' 
carac = input("Ingrese un caracter: ")

if (carac == "\""):
    print("Es comilla doble ")
elif  (carac=="'"):
    print("Es comilla simple")    
else:
    print("No es comilla")