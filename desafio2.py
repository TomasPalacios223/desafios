
"""comprueba si un numero ingresado por teclado es multiplo de 2, 3 o 5"""


num= int(input("Ingrese un numero  : "))


if (num%2==0):
    print("El numero ingresado es multiplo de 2")
if (num%3==0):
    print("El numero ingresado es multiplo  de 3")
if (num%5 ==0):
    print("El numero ingresado es multiplo 5")
if ((num%2!=0)and (num%3!=0)and(num%5 !=0)):
    print("el numero ingresado no es multiplo de 2, 3 ni 5")