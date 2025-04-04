# Nota; brake para salir de un while
from ast import Break
""" nume= int(input("digite un numero entero positivo para ver su tabala de multiplicacion del 1 al 10 "))
cont= 1
while cont <= 100:
    nume *= cont
    cont += 1
    if cont == 10:   #cuando llegue a 10, sale del bucle. 
        Break """ 
# Hacer una tabla en condiciones
cel= 0 
print("tabla de temperatura")
print("*"*34)
print("grados celsius\t*\tgrados fahrenheint")
print("*"*34) 
for cel in range (0,110,10):
    far= (cel*9/5)+32
    print(f"*\t{cel}\t*\t{far}\t*\n")
    print("*"*34) 
