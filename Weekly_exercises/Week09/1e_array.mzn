int: n;
array[1..n] of var 0..9: numbers;

constraint sum(numbers) == product(numbers);

constraint forall(i in 1..n-1)(
  numbers[i] <= numbers[i+1]
 );

solve satisfy;

output["Array: ", show(numbers), "\n"];