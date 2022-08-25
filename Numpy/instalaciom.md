#  - Clase Instalacion - Numpy


# ESTAMOS IMPORTANTO NUESTRA PRIMER LIBRERIA
import numpy as np


De todos los metodos que vimos, resaltamos:

- .shape / .reshape( , ) 
- np.random.
- [ : ] recortes
- .max() / .min() / .sum() / .mean()
- np.median() 
- np.concatenate


import pandas as pd

# para poder levantar el archivo en colab, debemos subirlo primero a nuestro entorno 
df = pd.read_csv('Salarios Openqube - 2020.02.csv',decimal ='.') <br>
datos = df['Salario mensual NETO (en tu moneda local)'] #busco por nombre de la columna <br>
datos = datos[datos != '39.434.784'].astype(float) #para simplificar la limpieza de los datos, elimino este valor y paso todo a numero decimal  <br>

## Ejemplos : 

sueldos_netos = np.array(datos,dtype=int)
sueldos_netos

sueldos_netos.max()

sueldos_netos.min()}

sueldos_netos = np.sort(sueldos_netos)

np.size(sueldos_netos)

#limpiemos estos datos extremos
#Recuerdan algo de estadistica??

print("La poisicion del 3er cuartil",6414*0.75)
print("La poisicion del 1er cuartil",6414*0.25)

np.sort(sueldos_netos)[1603:4811]

np.median(sueldos_netos)

np.var(sueldos_netos) #varianza
np.std(sueldos_netos) # desvio estandar

# otro de los tantos metodos, no permite calcular directo los cuartiles
np.quantile(sueldos_netos,[0.25,0.5,0.75])

# Ejercicios con Matrices

#Ejercicios

lista_de_listas=[ [-44,12], 
                  [12.0,51], 
                  [1300, -5.0]]

np.zeros(10,dtype=int)


# contruir una matriz 
#np.array(elemento_X)
mi_matriz = np.array(lista_de_listas,dtype=int)
print("Matriz original")
print(mi_matriz)