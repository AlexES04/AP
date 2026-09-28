int: n;
int: x;
array[1..n] of int: value;

set of int: HOUSES = 1..n;

array[HOUSES] of var 0..1: taken;
var int: total_value;

constraint forall(house in 1..n-1)(
  taken[house] + taken[house+1] <= 1
);

constraint sum(taken) <= x;

constraint total_value = sum(house in HOUSES)(taken[house] * value[house]);

solve maximize total_value;

output["taken = ", show(taken), "\n", "total_value = ", show(total_value), "\n"];