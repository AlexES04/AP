include "globals.mzn";
set of int: R = 1..9;

array[R,R] of var R: s;

constraint forall(row in R)(
  alldifferent([s[row, column] | column in R])
);

constraint forall(column in R)(
  alldifferent([s[row, column] | row in R])
);

constraint forall(r_base in {1, 4, 7}, c_base in {1,4,7})(
  alldifferent([s[r, c] | r in r_base..r_base+2, c in c_base..c_base+2])
);

solve satisfy;