int: n;
array[1..n] of int: nota;        

int: max_caramelos = 100000;
array[1..n] of var 1..max_caramelos: x;
var int: total_caramelos;

constraint forall(i in 1..n-1)(
  if nota[i] == nota[i+1]
  then x[i] == x[i+1]
  elseif nota[i] > nota[i+1]
  then x[i] > x[i+1]
  else x[i] < x[i+1]
  endif
);

constraint max(x) < (min(x)*2);
constraint total_caramelos = sum(x);

solve minimize total_caramelos;

output ["Caramelos = ", show(x), "\n", "Total de caramelos = ", show(total_caramelos), "\n"];