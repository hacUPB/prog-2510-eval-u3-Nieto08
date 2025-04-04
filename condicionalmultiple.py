"""match"""
print ("*" * 60)  # para imprimir 60 veces "*" ese caracter
print ("calculadora")
print ("*" * 60)

print("S. sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nP. Potencia")
opcion= input("elija la opcion: ").upper()
num1 = float(input("ingrese número 1: "))
num2 = float(input("ingrese número 2: "))

match opcion:
    case "S":
        res = num1 + num2
    case "R":
        res = num1 - num2
    case "M":
        res = num1 * num2
    case "D":
        if num2 != 0:
            res = num1 / num2
        else:
            res= "indewrterminado"
    case "P":
        res = num1 ** num2     
    case _:
        print("opcion no válida")
print(f"el resultado es {res:0.2f}")


