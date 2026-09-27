int: num_nodes;
int: num_edges;

1..num_nodes: source;
1..num_nodes: sink;

array[1..num_edges, 1..2] of int: edges;
array[1..num_edges] of int: capacity;

var int: max_flow;

array[1..num_edges] of var int: flow;

constraint forall(i in 1..num_edges)(
  flow[i] >= 0 /\ flow[i] <= capacity[i]
);

constraint forall(n in 1..num_nodes where n != source /\ n != sink)(
  sum(i in 1..num_edges where edges[i,1] == n)(flow[i]) == sum(i in 1..num_edges where edges[i,2] == n)(flow[i])
);

constraint max_flow = sum(i in 1..num_edges where edges[i,2] == sink)(flow[i]);

solve maximize max_flow;


output["max flow = ", show(max_flow), "\n", "Edges: ", show(edges)];