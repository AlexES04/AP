int:n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

var set of ITEMS: taken;
var int: total_value;

constraint sum(item in taken)(weight[item]) <= capacity;
constraint total_value = sum(item in taken)(value[item]);

solve maximize total_value;

output["taken = ", show(taken), "\n", "Total Value = ", show(total_value), "\n"];