# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

texto = input("Escribe un texto: ")
lista = []
contador = 0
i = 0
exito = False
cadena =""
division = texto.split()
posiciones=[]
#!/usr/bin/env

for word in division:
    lista.append(word)
    contador = contador + 1
    
numero = int(input("Dime un numero contenido entre 1 y {}: ".format(contador)))

adivina = lista[numero - 1]

print("Adivina la palabra: {}".format(adivina))
caracter = input("Introduce un caracter de la palabra: ")
z=0
for character in adivina:
    if caracter in adivina:
        exito = True and posiciones.append(z)
        
    z = z + 1
    
print("estas son las posiciones del caracter: {}".format(posiciones))
if exito == True:
    numeroletras = len(adivina)
    print(numeroletras)
    for i in range(numeroletras):
      cadena = cadena + "*"
    print (cadena)
    print("Este caracter {} esta presente en {} en la posicion {}".format(caracter, adivina, posiciones))
else:
    print("Este caracter {} NO esta presente en {} ".format(caracter, adivina))
        
   
        
    
#print(numero)
#print(texto)
#print(lista)
