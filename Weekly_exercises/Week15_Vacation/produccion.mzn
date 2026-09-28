include "globals.mzn";

enum Q = {q1, q2, q3, q4, q5, q6, q7};
set of int: VALORES = 1..6;

array[1..5] of var VALORES: tiradas;
array[1..6] of var Q: estados;

constraint estados[1] = q1;
constraint estados[6] = q5;

constraint forall(i in 1..5)(
  ((estados[i] == q1 /\ tiradas[i] in {1,2,4,6}) -> (estados[i+1] == q1))
  /\
  ((estados[i] == q1 /\ tiradas[i] == 3) -> (estados[i+1] == q2))
  /\
  ((estados[i] == q1 /\ tiradas[i] == 5) -> (estados[i+1] == q3))
  /\
  ((estados[i] == q2) -> (
    if tiradas[i] in {1,2} then estados[i+1] == q4
    elseif tiradas[i] in {3,4,5,6} then estados[i+1] == q3
    endif
  )) 
  /\
  ((estados[i] == q3) -> (
    if tiradas[i] in {3,4,5} then estados[i+1] == q1
    elseif tiradas[i] == 6 then estados[i+1] == q6
    elseif tiradas[i] == 2 then estados[i+1] == q2
    else estados[i+1] == q1
    endif
  )) 
  /\
  ((estados[i] == q4) -> (
    if tiradas[i] in {3,4,5, 6} then estados[i+1] == q3
    else estados[i+1] == q5
    endif
  )) 
  /\
  ((estados[i] == q5) -> (
    if tiradas[i] in {3,4,5,6} then estados[i+1] == q3
    else estados[i+1] == q1
    endif
  )) 
  /\
  ((estados[i] == q6) -> (
    if tiradas[i] in {4,5,6} then estados[i+1] == q7
    else estados[i+1] == q6
    endif
  ))
);

solve satisfy;