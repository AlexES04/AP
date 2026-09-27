enum Women = {Maria, Ana, Lucia};
enum Men = {Carlos, Marco, Juan};

array[Women, Men] of int: wrank = [|1,2,3|3,2,1|2,3,1|];
array[Men, Women] of int: mrank = [|2,1,3|1,2,3|1,3,2|];

array[Men] of var Women: wife;
array[Women] of var Men: husband;

var int: obj_men;
var int: obj_women;

constraint forall(m in Men)(
  (husband[wife[m]] = m)
);

constraint forall(w in Women)(
  (wife[husband[w]] = w)
);

constraint forall(m in Men, w in Women)(
  not(mrank[m, w] < mrank[m, wife[m]] /\ wrank[w, m] < wrank[w, husband[w]])
);

constraint obj_men = sum(m in Men)(mrank[m, wife[m]]);
constraint obj_women = sum(w in Women)(wrank[w, husband[w]]);

solve minimize abs(obj_men - obj_women); 

output["wife: ", show(wife), "\n", "husband: ", show(husband), "\n", "obj_men: ", show(obj_men), "\n", "obj_women: ", show(obj_women), "\n"];