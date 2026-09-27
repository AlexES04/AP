# Semana 4b - DFS: _Topological Sort Recursive_
## ================= ENUNCIADO =================

    """
 La solucion que retorna esta función es un diccionario de Python.
   * La clave del diccionario es el número del nodo
   * El valor es el orden topologico asignado a ese nodo
 
 Por ejemplo, si tenemos el siguiente grafo dirigido con 3 vertices:
                    3 ---> 2 ---> 1
 ... el orden topologico es:
                El vértice 3 va en la primera posición
               El vértice 2 en la segunda posición
               El vértice 1 en la tercera posición
Con lo que debemos devolver un diccionario con este contenido:    {1: 3, 2: 2, 3: 1}