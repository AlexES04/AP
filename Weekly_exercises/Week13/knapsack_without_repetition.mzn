int: N = 3;
set of int: ITEMS = 1..N;

array[1..N] of int: value = [45, 48, 35];
array[1..N] of int: weight = [5, 8, 3];
int: capacity = 10;

array[1..N] of var 0..1: taken;
var int: total_value;

constraint sum(i in ITEMS)(taken[i] * weight[i]) <= capacity;

total_value = sum(i in ITEMS)(taken[i] * value[i]);

solve maximize total_value;


output["taken = ", show(taken), "\n", "Total value = ", show(total_value), "\n"];

