import random
titulo= str(input("es usted señor a señora: ")).lower()
while titulo not in ["sr", "sra", "señor", "señora"]: #informacion sacada de deepseek, evalúa sí titulo está bien escrito.
    titulo= input("por favor ser más clar@, es usted señor o señora: ") 
nombre= str(input("por favor digame sus nombres y apellidos: "))
print("*"*50)
print (f"Bienvenido {titulo} {nombre} a aerolineas hello world")
print("*"*50)
destino= int(input("seleccione el número asignado a su destino: \n1. Medellín\n2. Bogotá\n3. cartagena.\n:* "))
while destino not in range (1,4):
    destino= int(input("seleccione un número válido, asignado a su destino: \n1. Medellín\n2. Bogotá\n3. cartagena.\n:* "))
origen= int(input("seleccione el número asignado de su origen: \n1. Medellín\n2. Bogotá\n3. cartagena.\n:* "))
while origen not in range (1,4):
    origen= int(input("seleccione un número válido, asignado de su origen: \n1. Medellín\n2. Bogotá\n3. cartagena.\n:* "))
cont= 0
if destino == origen:
    destino=int(input("por favor seleccionar otro destino, que no sea el mismo origen:\n1. Medellín\n2. Bogotá\n3. cartagena.\n:*  ")) 
if destino==1:
    destinot= "Medellín"
    
elif destino==2:
    destinot= "Bogotá"
    
elif destino==3:
    destinot= "Cartagena"
if origen == 1:
    origent= "Medellín"

elif origen == 2:
    origent= "Bogotá"

elif origen==3:
    origent= "Cartagena"

while destino!= origen and cont == 0:
    if destino or origen== 1 and origen or destino== 2: 
        distancia= 240
    elif destino or origen== 1 and origen or destino== 3: 
        distancia= 461
    elif destino or origen== 2 and origen or destino== 3: 
        distancia= 657  
    cont+= 1
diad=int(input("seleccione un número asignado a un dia: \n1. lunes\n2. martes\n3. miercoles\n4. jueves\n5. viernes\n6. sábado\n7. Domingo\n*"))
if diad== 1:
    dia= "Lunes"
elif diad== 2:
    dia= "Martes"
elif diad== 3:
    dia= "Miércoles"
elif diad== 4:
    dia= "Jueves"
elif diad== 5:
    dia= "Viernes"
elif diad== 6:
    dia= "Sábado"
elif diad== 7:
    dia= "Domingo"
mesd=int(input("escriba el mes del vuelo :\n1. enero\n2. febrero\n3. marzo\n4. abril\n5. mayo\n6. junio\n7. julio\n8. agosto\n9. septiembre\n10. octubre\n11. noviembre\n12. diciembre\n* "))
for i in range (diad):
    if i in range (1,4):
        if distancia<400:
            precio= 79,900
        elif distancia>=400:
            precio= 156,900
    elif i in range (5,7):
        if distancia<400:
            precio= 119,900
        elif distancia>=400:
            precio= 213,000
asiento_tip= int(input("prefiere un asiente \n1. en pasillo pasillo\n2. junto a la ventana\n3. no tiene preferencia\ningrese el numero de su preferencia: "))
if asiento_tip==1:
    asiento_tip= "C"
elif asiento_tip==2:
    asiento_tip= "A"
elif asiento_tip==3:
    asiento_tip= "B"
else:
    print("opcion no valida, se asignará un asiento aleatorio")
    asiento_tip=random.choice(["A", "B", "C"]) #asigna una letra aleatoria
numero= random.randint(1,29) #genera un número random entre el 1 y el 29
asiento_ram= (f"{numero}{asiento_tip}")
print(f"Gracias por elegirnos sobre avianca, {titulo} {nombre}, su vuelo desde {origent} con destino a {destinot} está confirmado para el dia {dia} del mes {mesd} a un costo de ${precio} pesos, con el asiento asignado de {asiento_ram}")