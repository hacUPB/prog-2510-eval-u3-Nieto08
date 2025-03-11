num= int(input("press 1. para repetir\n prees 2. para fin:\n "))
while(num!=2):
    print ("*" * 60)
    print ("calculadora")
    print ("*" * 60)

    print("S. sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nP. Potencia")
    opcion= input("elija la opcion: ").upper()
    num1 = float(input("ingrese número 1: "))
    num2 = float(input("ingrese número 2: "))

    if opcion.upper() == "S":
        res = num1 + num2
    elif opcion.upper() == "R":
        res = num1 - num2
    elif opcion.upper() == "M":
        res = num1*num2
    elif opcion.upper() == "D":
        if num2 != 0:
            res = num1/num2
        else: 
            res= "inderterminado"
            print("div por 0")    
    elif opcion.upper() == "P":
        res = num1**num2
    else: 
        print ("elija una letra de las válidas")
    print (f"el resultado es: {res:0.2f}")  
    num= int(input("press 1. para repetir\n prees 2. para fin:\n "))
else:
    print ("fin")  