include "globals.mzn";

int: numCities;          % número de ciudades
set of int: City = 1..numCities; 
int: maxAllowedEdge;     % máxima distancia permitida de un trayecto del recorrido

array[City,City] of int: distance; 

var int: maxEdge;
array[City] of var City: succ;

constraint circuit(succ);
constraint maxEdge = max(i in City)(distance[i, succ[i]]);
constraint maxEdge <= maxAllowedEdge;

constraint forall(i in City)(
  distance[i, succ[i]] != -1
);

solve minimize maxEdge;

output["succ = ", show(succ), "\n", "maxEdge = ", show(maxEdge), "\n"];