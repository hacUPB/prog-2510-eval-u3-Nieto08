import random
count= 1
num_secret= random.randint(1,100)
num_player= int(input("Bienvenido al juego, ingrese su número: "))
while num_player != num_secret:
    if num_player < num_secret:
        print("el número es mayor, intenta otra vez")
        num_player= int(input("ingrese otro número: "))
    elif num_player > num_secret:
         print("el número es menor, intenta otra vez")
         num_player= int(input("ingrese otro número: "))   
    count+=1  #en el quiz, este count no está iterado, quedó fuera del while 
print(f"¡Felicidades!, has adivinado el número {num_secret} en {count} intentos")
print("este código fue creaddo por Juan Sebastian Nieto Contreras, id: 000474009")

