#ESTRUCTURAS DE CONTROL IF - WHILE - FOR

#VARIABLES 

contador = 0

contador += 1
contador += 1
contador += 1

print(contador)

#TIPADO DINAMICO
contador = "Hola"
print(contador)

#ESTRUCTURAS DE CONTROL

condicion = True #False 

#IF

if condicion:
    print("La condicion es verdadera")
    
else:
    print("La condicion es falsa")

#Si quiero hacer un swtich hago if encadenados 

#FOR

for i in range(0, 10):
    print(i)

lista = ["Hola", "Si", "Adios"]

for palabra in lista:
    print(palabra)

#WHILE

condicion = True

while condicion:
    contador += 1
    print (contador)
    
    if contador > 12:
        break

print("Adios")
