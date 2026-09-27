# Algoritmos y Programación

## Tema 1 - Análisis de la eficiencia algorítmica

El análisis de un algoritmo consiste en medir su eficiencia, ya sea mediante una estrategia empírica o analítica, buscando una expresión que represente, finalmente, el **coste asintótico** del algoritmo. En esta expresión no se tienen en cuenta las constantes o los términos de menor grado. De hecho, por lo general, en el análisis asintótico se prefiere usar únicamente el término de mayor exponente.

### 1.1 - Notaciones asintóticas

En el análisis asintótico de un algoritmo, se debe de aprender la definición de _ejemplar de un problema_, que es cada uno de los posibles casos que se pueden dar como datos iniciales del problema. Teniendo esto en cuenta, se deben llevar a cabo tres pasos:

- Definir N: N es número de bits necesarios para codificar un ejemplar. Básicamente, es el número de vueltas que da un algoritmo, por ejemplo, si un algoritmo se dedica a recorrer una estructura de datos, N será el número de elementos que contenga la estructura. Por otro lado, en un grafo, N vendrá determinada por la razón entre el número de vértices y aristas en un grafo.

- Casos de estudio: En el caso de que los ejemplares del problema sean del mismo tamaño, se analizará el mejor caso, el peor caso y el caso promedio.

- Reglas generales para el análisis asintótico:
    - El Orden de una operación elemental es 1.
    - El Orden de una secuencia de operaciones se calcula aplicando la regla de la suma, que vendrá determinado por el máximo de las dos operaciones.
    - El Orden de una sentencia condicional es igual al máximo del Orden de cada alternativa.
    - El Orden de un bucle es igual al Orden de la suma de sus iteraciones.
    - El Orden de una llamada a un subprograma es igual al Orden del subprograma llamado.

En realidad, resulta innecesario calcular el orden de todas las operaciones puesto que es suficiente con determinar la operación elemental que se ejecuta el mayor número de veces, es decir, la **operación crítica**.

### 1.2 - Analísis de eficiencia de algoritmos iterativos

Entre los algoritmos de ordenación iterativos, se distinguen tres tipos: ordenación por selección, ordenación por inserción y burbuja.

Los algoritmos de ordenación por selección consiste en, mientras queden elementos en la lista de entrada, buscar el menor elemento y se extrae de la lista de entrada y se añade a la lista de salida. Hay una variante de este algoritmo denominada _in place_, que utiliza la misma lista de entrada como de salida, o sea, va modificando la propia lista de entrada.

La algoritmos de ordenación por inserción consiste en recorrer los elementos de la lista de entrada e insertarlos en su posición correcta en la lista de salida. Este es un buen ejemplo para explicar los posibles casos de estudio: el mejor caso sería aquel en el que la lista estuviera ordenada (O(n)), el peor caso sería aquel en el que la lista estuviera en orden inverso (O(n<sup>2</sup>)), y el caso promedio sería aquel en el que la lista está en orden aleatorio (O(n<sup>2</sup>)).

La algoritmos de ordenación por burbuja consiste en recorrer los elementos de la lista comparando el elemento i con el i+1 e intercambiando su posición en caso de que i+1 sea menor. En este caso, el hecho de comprobar que se haya realizado algún intercambio en los elementos o no, define un algoritmo más eficiente.

### 1.3 - Análisis de eficiencia de algoritmos recursivos

En los algoritmos recursivos, lo primero que hay que hacer es obtener la recurrencia. Para ello, se establece el tamaño del ejemplar dependiendo de los parámetros del algoritmo, se añade el coste de las llamadas recursivas y el coste de ejecución de la parte iterativa y se identifica y añaden los casos base.

Una vez obtenida la ocurrencia, se resuelve aplicando una de las tres formas posibles: método de sustitución (_Guess and Test_), teorema maestro o herramientas de resolución (_solver_) de recurrencias.

## Tema 2 - Estrategias de diseño algorítmico

Entre las estrategias que se pueden emplear para el diseño de un algoritmo, existen distintas opciones aplicables a escenarios distintos.

### 2.1 - Fuerza bruta

La estrategia de **fuerza bruta** se basa en la definición del problema y evalúa todas las posibles combinaciones que resuelven el problema. Debido a esto, es aplicable en muchos casos, es simple y genera soluciones razonables. 

Sin embargo, esta estrategia tiene una enorme desventaja y es que, al tener que generar todas las combinaciones posibles, estos algoritmos resultan muy poco eficientes por la posible ocupación de espacio y tiempo de generación que se pueda dar.

Los algoritmos de fuerza bruta se pueden realizar mediante un código iterativo, un código recursivo o con un iterador.

### 2.2 - Ávida (_greedy_)

La estrategia ávida, avariciosa o voraz (_greedy_) se implementa mediante un bucle donde, en cada paso, se dispone de un conjunto de candidatos, se elige el "mejor" y lo añade a la solución. Este algoritmo **nunca** deshace las soluciones tomadas. Dos de los algoritmos más famosos que usan estrategia _greedy_ son el de _Dijkstra_ y el de _Kruskal_.

Por ejemplo, en el problema de devolución del cambio donde, con una cantidad N a devolver, se tiene que calcular el número mínimo de monedas para devolver. Inicialmente, se reordenan las monedas de mayor a menor valor, se reocrre la lista y se elige siempre la de mayor valor que se acerca al objetivo. 

Este algoritmo es muy eficiente, pero no funciona bien siempre, ya que solo funciona en problemas donde la decisión del algoritmo coincide con la decisión correcta. Dicho esto, para que un algoritmo de _greedy_ funcione correctamente, se debe cumplir la siguiente propiedad: el valor de cada tipo de moneda es mayor o igual que el doble del valor que le precede.

Resulta interesante de mencionar la la compresión de ficheros, donde se necesita generar un código que minimice la cantidad de bits que se debe utilizar para codificar un texto. Este código se ha mejorado empleando el **código de Huffman**, que consiste en asignar códigos más pequeños a las palabras más frecuentes/repetidas. Primero, se crea un nodo por cada letra y se guarda su frecuencia en el nodo, luego se eligen los nodos raíz con menor frecuencia y se unen para formar un subárbol binario asignando al nuevo nodo raíz la suma de las frecuencias de sus nodos hijos, y se repiten estos dos pasos hasta el final. Este código se emplea en la compresión de archivos gzip y en la codificación de multimedia (JPEG y MP3).

### 2.3 - Divide y vencerás

La estrategia de divide y vencerás consiste en romper el problema recursivamente en dos o más subproblemas del mismo tipo hasta que estos seean lo suficientemente simples como para resolverse de manera directa. La solución al problema original vendrá dada por la combinación de las soluciones de los subproblemas.

Por ejemplo, se da el problema de buscar el máximo de un conjunto de números. Se tienen que dar tres características: el factor de reducción debe ser grande, no puede existir solapamiento entre subproblemas y estos deben ser independientes para resolverse en paralelo.

El algoritmo de ordenación _merge sort_ emplea la estrategia de divide y vencerás, donde parte la lista inicial en dos y, esas dos partes, las vuelve a dividir en dos. Otro algoritmo de ordenación es el _quick sort_, que usa un pivote aleatorio para colocar los elementos a su izquierda (menores) o su derecha (mayores). En este algoritmo se debe usar siempre el primero o último elemento como pivote cuando los números están desordenados. En el caso de que no sea así, el algoritmo no será eficiente.

### 2.4 - Vuelta atrás (_backtracking_)

Para describir la estrategia de _backtracking_, primeramente, se pondrá el caso de la fuerza bruta en un ejercicio de buscar las combinaciones de 3 variables binarias donde no haya números contiguos repetidos.

Cada variable, es decir, cada valor binario será asociado a un nivel de profundidad, de modo que, en este caso, se tendrán 3 niveles de profundidad. El algoritmo de fuerza bruta generaría todas las combinaciones posibles y se quedaría con las soluciones válidad. El algoritmo de _backtracking_, por su parte, cuando una solución no es válida en cualquier nivel de profundidad, la descarta, vuelve para atrás y sigue con las combinaciones. 

Dicho de otro modo, el algoritmo de _backtracking_, construye candidatos parciales donde cada uno añade un componente a la solución (un nivel más de profundidad) y descarta los candidatos que no llevan a una solución posible. Los candidatos se pueden representar como nodos en un árbol.

### 2.5 - Programación dinámica

La **programación dinámica** es una técnica dedicada a resolver problemas de optimización que se refiere a la planificación dinámica de decisiones. Esta consiste en resolver un problema complejo descomponiéndolo en subproblemas más simples que se resuelven una sola vez y se combinan. 

Se suele utilizar cuando los subproblemas de un problema original se solapan y tienen subestructura óptima.

Al contrario que la estrategia _greedy_, la programación dinámica se usa cuando los subproblemas se solapan y tienen subestrcutura óptima. Además, busca un factor de reducción pequeño y guarda los resultados intermedios (de los subproblemas) en una memoria o tabla (como, por ejemplo, los valores en una resolución de Fibonacci) para evitar repetir cálculos.

En cuanto a la implementación de programación dinámica, se puede realizar de dos maneras:
- Memoization: el problema se resuelve recursivamente (_top-down_).
- Tabulation: el problema se resuelve comenzando por los subproblemas o iterativamente (_bottom-up_).

El rendimiento de las dos implementaciones depende del tamaño del problema; en problemas pequeños, _Tabulation_ es más eficiente porque no tiene llamadas recursivas, pero, en problemas grandes, _Memoization_ puede ser mejor ya que consume menos memoria.

## Tema 3 - Complejidad computacional
### 3.1 - Complejidad computacional de un problema. Problemas P vs NP

La teoría de la complejidad computacional se centra en la clasificación de los problemas computacionales de acuerdo con su dificultad inherente. Un problema inherentemente difícil es aquel cuya solución requiere de una cantidad significativa de recursos computacionales sin importar el algoritmo empleado.

Uno de los objetivos de la teoría de la complejidad computacional es determinar los límites prácticos de lo que se puede hacer con una computadora, analizando todos los posibles algoritmos que pueden ser utilizados para resolver el mismo problema. Básicamente, esta teoría se preocupa por qué tipo de problemas pueden ser resueltos con una cantidad determinada de recursos o, dicho de otro modo, de manera algorítmica. Resulta importante mencionar la máquina de Turing, que, en un principio, se creó como una máquina capaz de resolver o computar cualquier secuencia computable, según la tesis Church-Turing. 

El teorema de Rice, que pertenece a la teoría de la computabilidad, afirma que no se puede escribir un programa que analice otro programa y determine cualquier aspecto interesante de su comportamiento, únicamente las propiedades triviales son decidibles. Por propiedad trivial se entiende una propiedad que todos los programas poseen o, en su defecto, ningún programa posee. Una propiedad indecidible, es decir, que no se puede determinar, sería, por ejemplo, saber si un programa produce una salida específica o si un programa termina para todas las entradas.

En cuanto a los tipos de problemas, en la práctica, los problemas que se pueden resolver son aquellos que tienen algoritmos en tiempo polinómico (tratables). Sin embargo, conocer si un problema tiene algoritmo en tiempo polinómico o no no es tan fácil. 

En general, existen cuatro problemas de búsqueda que son los fundamentales. Estos son:
- LSOLVE: resolver un sistema de ecuaciones lineales con una variable real [ Tratable por Gauss-Jordan ].
- LP: resolver un sistema de inecuaciones lineales con variable real [ Tratable por algoritmo del elipsoide ].
- ILP: resolver un sistema de inecuaciones lineales con variable entera (0/1) [ Intratable ].
- SAT: resolver un sistema de ecuaciones booleanas (encontrar solución binaria)[ Intratable ].

Los **problemas NP** (_Nondeterministic Polynomial_) son todos los problemas de decisión, es decir, de SÍ o NO, que tienen una solución factible la cual se puede comprobar en tiempo polinómico. Por ejemplo, factorizar un número grande es difícil de resolver, pero comprobar las soluciones es sencillo. Otra definición para los problemas NP sería aquellos problemas que pueden ser resueltos por una máquina de Turing no determinista en tiempo polinómico. Los **problemas P** (_Polynomial_) son todos los problemas de decisión que se resuelven en tiempo polinómico.

Aquí surge la duda de si NP = P. Para ello, se emplea la Reducción de Cook, que dice que "Si un problema X puede reducirse en tiempo polinómico a otro problema Y, decimos que resolver Y es al menos tan difícil como resolver X". Luego, el Teorema de Cook-Levin afirma que todo problema NP puede reducirse en tiempo polinómico a SAT, garantizando que resolver SAT es al menos tan difícil como resolver cualquier problema NP.

Por otro lado, un problema **NP-Completo** es aquel para el cual todos los problemas NP se pueden reducir a él, por ejemplo, SAT. Gracias al Teorema de Cook-Levin se obtiene esta categoría, garantizando, de nuevo que, si se pudiera resolver SAT en tiempo polinómico, se podrían resolver todos los problemas NP.

Un problema **NP-Hard** es aquel para el cual todos los problemas NP se pueden reducir a él, pero él mismo no tiene por qué estar en NP, pudiendo ser, incluso, más difícil o indecidible. Por ejemplo, la versión de optimización del problema TSP (Problema del Agente Viajero), donde, dado un conjunto de ciudades y distancias entre ellas, se debe encontrar la ruta más corta que visita cada ciudad exactamente una vez y regresa al punto de partida. La versión de decisión del problema es NP-Hard porque se plantea la pregunta de "¿existe una ruta con costo <= K?". Aquí se vuelve a las propiedades indecidibles, no es trivial, por ello es NP-completa. Ahora bien, resolver la versión de optimización permitiría resolver la de decisión, por ello la optimización es al menos tan difícil como cualquier problema NP, aunque no pertenece a NP, ya que no es de decisión.

### 3.2 - Ramificación y Acotación (_Branch and Bound_)

Cuando se habla de la formalización de un problema, hay tres cosas primordiales que se tienen que definir: variables de decisión, restricciones y función objetivo. En una formulación declarativa, el objetivo, en vez de inclinarse a plantear cómo resolver el problema, se inclina a especificar cómo representarlo.

Los algoritmos de ramificación y acotación tienen 2 pasos iterativos claros que se indican en su nombre, precisamente. La ramificación consiste en dividir el problema en subproblemas y la acotación denota la búsqueda de una estimación óptima de la mejor solución del subproblema, pudiendo maximizar (límite superior) o minimizar (límite inferior).

Al usar un DFS en un algoritmo de _Branch and Bound_ se posee la ventaja de que no requiere almacenar todos los nodos simultáneamente y de que se puede usar la memoria lineal en función de la profundidad del árbol. Eso sí, al hacerlo de esta manera, puede que se exploren ramas no prometedoras antes de podarlas. Por el contrario, al usar BFS, siempre se explora el nodo más prometedor a continuación y el algoritmo pasa a tener un potencial grande para encontrar soluciones óptimas rápidamente. Sin embargo, también tiene un inconveniente, y es que requiere almacenar todos los nodos en la frontera, lo que puede llevar a consumir mucha memoria.

## Tema 4 - Programación declarativa
### 4.1 - Introducción a la programación declarativa

Para entender el concepto de programación declarativa, hay que definir otro concepto denominado **programación con restricciones**. Este se refiere a un tipo de programación que consiste en reducir el conjunto de valores que una variable puede tomar en base a unas restricciones establecidas, devolviendo resultados exactos.

### 4.2 - Programación con restricciones

En la programación con restricciones se deben realizar dos pasos: comprobar si cada restricción se puede cumplir correctamente (_feasibility checking_) y eliminar todos los valores de almacenamiento de dominio (_domain store_) que incumplan alguna restricción (_pruning_).

Otro concepto interesante es el **reificación** de una restricción, que consiste en transformar o crear otra restriccióncon una variable binaria tomando un valor positivo (1) si la restricción inicial se cumple o, en el caso contrario, un valor negativo (0).

En este punto, aparecen las **series mágicas**. Una serie mágica es una secuencia donde S<sub>i</sub> representa el número de ocurrencias de i. Es decir, la posición de cada número describe exactamente cuántas veces aparece ese número de posición dentro de la propia secuencia.

Por ejemplo, para la secuencia de números "0,1,2,3,4", una solución válida para que sea mágica podría ser (2,1,2,0,0), porque hay, efectivamente dos 0 (para el 3 y el 4), un 1 y dos 2 (para el 0 y el 2).

Para que se cumpla este fenómeno, se deben cumplir dos restricciones: la suma total de los números de la solución debe ser igual a la longitud de la serie y la suma de cada valor multiplicado por su posición también debe ser igual a la longitud de la serie.

Por otro lado, en el caso de que se empleen variables de decisión como índices en _arrays_, se le conoce como **_element constraint_**. Además, añadir restricciones redundantes pueden permitir al resolutor reducir el espacio de búsqueda y propagar valores de manera eficiente con la ventaja de que, realizar esto, no añade información adicional al modelo. Si se lleva esta idea al límite, se obtiene el concepto de **modelos duales**.


# NO SE DAN LOS SIGUIENTES TEMAS

## Tema 5 - Algoritmos aproximados
### Tema 5.1 - Algoritmos de aproximación rho-Aproximados
### Tema 5.2 - Esquemas de Aproximación de Tiempo Polinómico (1-e)

## Tema 6 - Algoritmos heurísticos y metaheurísticos
### 6.1 - Heurísticas y búsqueda local
### 6.2 - Metaheurísticas. Funciones objetivo no lineales y multiobjetivo

## Tema 7 - Programación entera mixta
### 7.1 - Programación Lineal, método Simplex
### 7.2 - Fundamentos de la Programación Entera Mixta
### 7.3 - Planos de corte. _Branch and Cut_
