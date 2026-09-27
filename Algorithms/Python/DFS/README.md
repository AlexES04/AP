# _Depth-First Search_ (DFS)

## Introducción

El algoritmo **_Depth-First Search_** (DFS) es un algoritmo de búsqueda no informada con un recorrido en profundidad. Esto significa que, imaginando el caso de un grafo o árbol, intenta ir lo más profundo posible antes de retroceder.

A nivel de programación, esto se consigue usando una pila (_stack_) como estructura de datos, que sigue el principio LIFO. Es un algoritmo sencillo que se consigue, prácticamente, en 5 pasos:
1) Se selecciona un nodo de origen, se marca como "visitado" y se introduce en la pila.
2) Se examina el nodo en la cima de la pila para saber si tiene nodos adyacentes (vecinos) que no hayan sido visitados. En ese caso, se elige uno de ellos, se marca como visitado y se introduce en la pila.
3) El paso 2 se repite iterativamente.
4) Cuando se alcanza un nodo que no tiene vecinos sin visitar, se extrae de la pila.
5) El algoritmo sigue extrayendo nodos de la pila y explorando las ramas alternativas hasta que la pila quede completamente vacía.

## Coste computacional
En cuanto al coste computacional del algoritmo DFS, se divide en dos:
- La **complejidad temporal** viene dada por el tiempo que el algoritmo consume en terminar. En el peor de los casos, el algoritmo visitará cada vértice (V) una vez y examinará cada arista (E) una vez (o dos en grafos no dirigidos), de modo que su costo es de O(V+E).
- La **complejidad espacial**, que se refiere al uso de memoria, vendrá dado por el tamaño máximo de la pila y la estructura que almacena los nodos visitados. En el peor de los casos, la profundidad máxima de la recursión será igual al número de vértices, así que su costo será de O(V).

## Explicación
### Recursivo
```python
def dfs_recursive(graph, first_node):
    N = graph.number_of_nodes()
    
    visited = set()

    def dfs(node):
        visited.add(node)

        for neighbour in graph.neighbors(node):
            if neighbour not in visited:
                dfs(neighbour)

    dfs(first_node)

    return visited
```

### Iterativo
```python
def dfs_iterative(graph, first_node):
    N = graph.number_of_nodes()

    visited = set()
    stack = Stack()

    visited.add(first_node)
    stack.push(first_node)

    while not stack.isEmpty():
        current = stack.pop()
        for neighbour in graph.neighbors(current):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.push(neighbour)
    return visited
```