list_cancion=["palabra","do the evolution","siguiendo la luna","ragamuffin","parte y choke","el pichón"]
list_artista=["sabue","pearl jam", "los fabulosos cadillacs","akapellah","jombriel","ryan castro"]
for i in range(0,6): # Tambien se puede colocar range(6):, que se inicializa igual en 0, hasta 6-1. 
    print(f"{list_cancion[i]} interpretada por {list_artista[i]}")
for cancion in list_cancion:
    print(cancion)
#le da valores 1 a 1 en cada interación y lo guarda en la variable canción. 