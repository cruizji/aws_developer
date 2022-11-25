#!/usr/bin/env
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

texto = input("Escribe un texto: ")
lista = []
lista2 = []
contador = 0
i = 0
exito = False
cadena =""
division = texto.split()
posiciones=[]


for word in division:
    lista.append(word)
    contador = contador + 1
    
numero = int(input("Dime un numero contenido entre 1 y {}: ".format(contador)))

adivina = lista[numero - 1]
acierto = False
intentos = int(len(adivina) + 1)
k = 0

print("La palabra a adivinar tiene {} caracteres".format(len(adivina)))
while acierto == False and contador <= intentos:
    caracter = input("Introduce un caracter de la palabra: ")
   
    if k == 0:
        for i in adivina : # Inicializar la lista y rellenarla con valores
            lista2.append("*")
         #   print(i)
            k = k + 1
        print(lista2)
        
    
    for index, character in enumerate(adivina):
        if caracter == character:
            lista2[index]=caracter
        else:
            exito = False
        #print(index)    
        
    if "*" in lista2:  # Chequear que la lista esta completa y se ha adivinado la palabra
        acierto = False
    else:
        acierto = True
        break
        
    restantes= intentos - contador
    print("estas son las posiciones del caracter: {} y tienes estos intentos {}".format(lista2, restantes )) 
    contador = contador + 1
    if restantes < 1:
        print ("!!!!!! :( You are not GOAT, bad luck !!!!!, the word to guess was: {}".format(adivina))
        raise SystemExit
      
        
print("--------------Nice !!!!!, You are GOAT (Greatest of all times)------------")
        
    
#print(numero)
#print(texto)
#print(lista)
