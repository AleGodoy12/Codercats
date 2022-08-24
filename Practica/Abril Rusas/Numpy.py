# # Ejercicios

# 1- Generar un array aleatorio de 100 elementos. Calcular la mediana correspondiente.

import numpy as np
array=np.random.randint(100,size=100)
print(array)

mediana=np.median(array)
print("La mediana es: ",mediana)

# 2- Recordar los ejercicios con funciones para cálculo de factorial y suma de serie. Repetir ambos ejercicios (puede ser sobre el mismo código), pero ahora utilizar las nuevas operaciones aprendidas con los ndarrays.
number=int(input("Ingrese un numero entero positivo: "))
Npa = np.array(range(1,number+1)) 
factorial=np.prod(Npa)
print("El factorial es: ",factorial)


serie=(Npa**2)  #Aca invente una serie  -->   serie=(n+1)**2 
print("Serie: ",serie)   
sumatoria=serie.sum()
print("La sumatoria de la serie es: ",sumatoria)