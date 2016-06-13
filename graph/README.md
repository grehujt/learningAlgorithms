## Graph Algorithms

algorithm | best | average | worst | key points
:---------|:------:|:---------:|:-------:|:-----------
Breadth-First Search | V+E | V+E | V+E | Graph, Queue
Depth-First Search | V+E | V+E | V+E | Graph, Recursion, Backtracking
Prim's Algorithm | (V+E)log(V) | (V+E)log(V) | (V+E)log(V) | weighted graph, binary heap, priority queue, greedy
Dijkstra's Algorithm PQ | (V+E)log(V) | (V+E)log(V) | (V+E)log(V) | Weighted directed graph, priority queue, overflow
Dijkstra's Algorithm DG | V^2 + E | V^2 + E | V^2 + E | weighted directed graph, overflow
Bellman-Ford Algorithm | V*E | V*E | V*E | weighted directed graph, overflow, all-pairs shortest path
Floyd-Warshall Algorithm | V^3 | V^3 | V^3 | dynamic programming, weighted directed graph, overflow
