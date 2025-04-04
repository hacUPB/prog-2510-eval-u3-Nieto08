estabilizado = False 
reingreso= False
orb= 0
ha= float(input("ingrese la altutud inicial del satélite en kilómetros: "))
coef= float(input("ingrese el coeficiente de arrastre esperado: "))
hs= float(input("ingrese la altitud minima de seguridad: "))
while ha <= hs:
    hs= float(input("ingrese una altitud minima de seguridad menor a la inicial: ")) 
while reingreso== False and estabilizado== False:
    hper= ha * coef
    if ha < hs:
        reingreso = True
    elif hper <= 0.001:
        estabilizado= True
    ha-= hper
    orb+= 1
if reingreso == True:
    print(f"El satélite Reingresó a la tierra despues de {orb} órbitas y su ultima altitud fue de {round (ha,3)} km")
else:
    print(f"El satélite se Estabilizó despues de {orb} órbitas y su ultima altitud fue de {round (ha,3)} km")