# Punto de reunión (Grafos con BFS)

## Contexto
Varias personas parten de diferentes posiciones (pudiendo haber varias personas en la misma posición) de una red de caminos bidireccionales (grafo no dirigido y sin pesos). Cada enlace (arista) representa un tramo y todos los tramos cuentan lo mismo. Se busca un punto de reunión donde la distancia que deba recorrer la persona más alejada sea lo más pequeña posible.

## Objetivo
Entre los caminos (lista de vértices) alcanzables por todas las personas, elegir el que minimice la mayor de las distancias mínimas desde sus posiciones iniciales (vértices).

Para un candidato v, habrá que calcular la distancia mínima desde cada posición hasta v y tomar la mayor. De entre todos los candidatos, se elige aquel con el menor valor de ese máximo, aclarando que no se minimiza la suma ni la media de las distancias.

NOTA: Un candidato es un vértice que se está considerando como posible punto de reunión. No es una persona ni un camino.

Dicho de otra forma, elige como punto de reunión un vértice al que puedan llegar todas las personas. Para cada posible punto, calcula la distancia más corta desde la posición de cada persona y toma la mayor de esas distancias. El punto elegido será aquel cuya distancia máxima sea menor.

##### Consideraciones:

- Cualquier vértice puede ser punto de reunión, aunque no sea una posición inicial.
- También se permite reunirse en la posición inicial de alguna persona.
- En caso de empate, se elige el vértice de menor identificador numérico.
- Si no existe un vértice alcanzable por todos, se indica que no hay solución.

### Formato de entrada
```python
N M K
p1 p2 ... pK
u1 v1
...
uM vM
```

- N: número de vértices, identificados con enteros desde 1 hasta N.
- M: número de aristas no dirigidas.
- K: número de personas.
- La segunda línea contiene exactamente K posiciones iniciales donde se permiten repeticiones porque varias personas pueden partir del mismo vértice pero el orden de las personas no afecta al resultado.
- Las siguientes M líneas contienen una arista no dirigida u v.

##### Consideraciones:
- Se cumple que N >= 1, M > 0 y K >= 1.
- Todos los identificadores pertenecen a 1..N.
- No hay bucles ni enlaces (aristas ) repetidos.
- Puede haber ciclos, componentes desconectadas y vértices aislados.

### Formato de salida
```python
Punto=P
DistanciaMaxima=D
```