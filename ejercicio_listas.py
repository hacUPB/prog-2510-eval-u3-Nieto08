texto= input("por favor coloque un código de al menos 30 palabras: ")
#separamos las palabras, y las contamos
cont_palabras= texto.split()
cont_palabras =len(cont_palabras)
print(cont_palabras)
#contamos la cantidad total con espacios, comas y puntos 
caracteres_cont= len(texto)
print(caracteres_cont)
#contar todo, excepto los espacios en blanco
cont_sin_espa= texto.strip(" ") #podemos poder lo que queramos entre los (), en este caso, es el espacio.
cont_sin_espa= len(cont_sin_espa)
print(cont_sin_espa)
#otra solucion es con el count, que sirve para contar los espacios en blanco y restarlos al total. texto.count(" ")
#contar cuantas veces aparece la letra "a" y "e"
letras_a= texto.lower().count("a")
letras_y= texto.lower().count("y")
print(f"a={letras_a} y y={letras_y}")