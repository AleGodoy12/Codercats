from array import array
import numpy as np
#1- Generar un array aleatorio de 100 elementos. Calcular la mediana correspondiente.
aleatorio= np.random.randint(100,size=100)
print(f"La mediana es {np.median(aleatorio)}")


#2- Recordar los ejercicios con funciones para cálculo de factorial y suma de serie. Repetir ambos ejercicios (puede ser sobre el mismo código), pero ahora utilizar las nuevas operaciones aprendidas con los ndarrays.
nros=(input("Ingresá una lista de números separados por ',' :"))
lista=nros.split(",")
cant=len(lista)

#Pasa los nros de la lista a type int
for n in range(cant):
    lista[n]=int(lista[n]) 

arrayA= np.array(lista) #Lo paso a array

total= np.sum(arrayA)
print(f"la suma de {arrayA} es {total}")

fact= np.math.factorial(total)
print(f"El factorial de {total} es: {fact}")
