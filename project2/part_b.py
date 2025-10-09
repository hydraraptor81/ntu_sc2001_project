import heapq
import time
import random
from generate import generate_vertices, generate_adjacency_list

def dijstra_list_heap(V, E, start):
    d = {node: float('inf') for node in V}      #distance to infinity
    pi = {node: None for node in V}             #predecessor map to None
    S = set()                                   #set of visted nodes
    d[start] = 0                                #start node to 0

    pq = [(0, start)]                           #initialize priority queue

    while pq:                                   #while priority queue not empty
        dist_u, u = heapq.heappop(pq)           #pop from priority queue, u: vetex with smallest distance
        if u in S: 
            continue
        S.add(u)                                #if unvisited, add to visited
        for v, w in E.get(u, []):               #v: neighbour of v, w: weight of edge connecting u to v
            if v in S:
                continue
            alt = dist_u + w                    #alternate path
            if alt < d[v]:
                d[v] = alt
                pi[v]= u
                heapq.heappush(pq, (alt, v))    #push new pair into priority queue

    return d, pi

def main():
    '''
    V = {"A", "B", "C"}
    E = {
        "A": [("B", 2), ("C", 5)],
        "B": [("A", 2), ("C", 1)],
        "C": [("A", 5), ("B", 1)]
    }
    '''
    random.seed(42)
    n = int(input("Enter the number of vertices: "))
    V = generate_vertices(n)
    E = generate_adjacency_list(V, n, no_edge_prob=-1)

    print("\nVertices (V):")
    print(V)

    print("\nEdges (E):")
    for node in sorted(E.keys()):
        print(f"{node}: {E[node]}")

    start_node = next(iter(V))                  # pick first node as start

    start_time = time.perf_counter()
    d, pi = dijstra_list_heap(V, E, start_node)
    end_time = time.perf_counter()
    time_taken = end_time - start_time

    print("\nDistances (d):")
    print(d)
    print("\nPredecessors (pi):")
    print(pi)
    print(f"\nTime taken: {time_taken:.9f} seconds")

if __name__ == "__main__":
    main()

