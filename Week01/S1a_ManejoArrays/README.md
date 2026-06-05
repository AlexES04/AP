# Semana 1a - Manejo de Arrays
## ================= ENUNCIADO =================
Dados 2 arrays, llamados Padre y Madre, generar un nuevo array mediante el cruce de orden de ambos que consiste en lo siguiente:
1. Se eligen dos puntos de corte aleatoriamente.
2. Entre estos dos puntos de corte, se sitúan los elementos del padre.
3. El resto se van eligiendo de la madre siempre que no hayan sido seleccionados previamente. Se comienza a partir del segundo punto de corte.


Por ejemplo, dada la siguiente entrada:

**parent1= [8,11,3,5,6,4,2,12,1,9,7,10]    #padre**

**parent2= [1,2,3,4,5,6,7,8,9,10,11,12]    #madre**

**lower_bound= 6                           #limite inferior**

**upper_bound= 9                           #limite superior**

Salida esperada:
**[4, 5, 6, 7, 8, 9, 2, 12, 1, 10, 11, 3]**
