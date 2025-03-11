orden= int(input("desea agregar otro plato?\n1. si \n2. no\n"))
while (orden!=2):
    print ("todos los platos vienen con la sopa del dia")
    orden_n= ("B. Bandeja paisa\nP. Pastel de garbanzo\nD. plato del dia\nE. ejecutivo\nS. solo sopa").upper()
    print("la sopa del dia es: sopa de ahuyama\n1. 1/2 de ahuyama\n2. ajo en polvo\n3. 1/2 zanahoria\n4. sal y especias")
    match orden_n:
        case "B":
            print ("-carne molida\n-chicharrón\n-chorizo\n-huevo frito\n-frisoles rojos\n-arroz blanco\n-arepa\n-tajada de platano\n-aguacate\n-ahogao")
        case "P":
            print ("-masa de maiz\n-garbanzo\n-carde de cerdo\n-arroz\n-ahogado\n-sal y especias")
        case "D":
            print ("-pechuga\n-papa criolla\n-mazorca\n-aguacate\n-ensalada de tomate")
        case "E":
            print ("-proteina\n-arroz\n-ensalada rusa\n-tajadas de maduro")
            proteina= int("elija la proteina: \n1.carne\n2.pollo\n3. cerdo")
        case "S":
             print("")
        case _:
            print("no ha seleccionado plato")
print("la orden es {orden_n}")
print ("fin")

            
        