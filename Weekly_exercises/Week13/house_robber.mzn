int: N = 5;
set of int: HOUSES = 1..N;

array[1..N] of int: value = [3, 10, 3, 1, 2];

array[1..N] of var 0..1: taken;
var int: total_value;

constraint forall(i in 1..N-1)(
  taken[i] + taken[i+1] <= 1
);

total_value = sum(i in HOUSES)(taken[i] * value[i]);

solve maximize total_value;

output["taken = ", show(taken), "\n", "Total value = ", show(total_value), "\n"];