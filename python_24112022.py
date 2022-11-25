
# Online Python - IDE, Editor, Compiler, Interpreter


########### Bucle itere 10 veces for
'''
i=1
for i in range(10):
     print(i)
'''     
#########Bucle itere 10 veces con while
'''
i=1
while i < 10:
 print (i)
 i = i + 1
'''
 ########### Adivinar tipo variable
'''
a=type(5)
b=type("hola")
print("El type de la variable a: {} + type de la variable b: {}".format(a,b))
''' 
############ Juego de adivina el número sin bucle
'''
import random
aleatorio=(random.randint(0,9))
usuario = input("Dime un numero")
if aleatorio == usuario:
 print ("Good luck, it´s the same")
else:
 print("Bad luck")
 '''
########## Juego de adivina el número con bucle

import random
aleatorio= 1
usuario=0
while aleatorio != usuario:
    aleatorio=(random.randint(0,9))
    usuario = input("Dime un numero")

    if aleatorio == usuario:
     print ("Good luck, it´s the same")
    else:
     print("Bad luck")
     
########## Leer csv y calcular media
import pandas as pd
import numpy as np

df = pd.read_csv("access-code.csv")
print(df.to_string())
media = df['Identifier'].mean() # Media columna
Identificador = df['Identifier'].sum() # Suma columna




