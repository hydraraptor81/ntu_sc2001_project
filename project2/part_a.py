import time
import random
from generate import generate_vertices, generate_adjacency_list, adjacency_list_to_matrix

def dijkstra_matrix_array(V, E, start):
    n = len(V)
    idx = {V[i]: i for i in range(n)}       #label -> index (e.g., "B" -> 1)
    dist = [float('inf')] * n               #distance to infinity
    S = [False] * n                         #list of visted nodes
    parent = [-1] * n                       #predecessor index to reconstruct paths

    if start not in idx:
        raise ValueError(f"Start node '{start}' not in V.")

    source = idx[start]
    dist[source] = 0                        #start node to 0

    for _ in range(n):
        # find unvisited node with smallest distance 
        u = -1                              #u: current node
        best = float('inf')
        for i in range(n):
            if not S[i] and dist[i] < best: #if not visited and the shortest distance
                best = dist[i]              #replace best with shortest distance
                u = i

        if u == -1:                         #no more reachable vertices
            break

        S[u] = True                         #mark visited node as True

        for v in range(n):
            weight = E[u][v]                      #v: neighbouring node of u, w: weight
            if S[v] or weight == float('inf'):
                continue                    #skip if node visted or no edge
            alt = dist[u] + weight
            #check if alternate path is shorter than current best path
            if alt < dist[v]:
                dist[v] = alt
                parent[v] = u

    d = {V[i]: dist[i] for i in range(n)}
    pi = {V[i]: (V[parent[i]] if parent[i] != -1 else None) for i in range(n)}

    return d, pi

def main():
    '''
    V = ["A", "B", "C"]

    #E: an adjacency matrix where:
    #E[i][j] is the weight of edge nodes[i] → nodes[j]
    #Use 0 on the diagonal (i == j)
    #Use float('inf') if there is no edge
    #start: the label of the source node, e.g. "A"

    E = [
        [0, 2, 5],   #A->A, A->B, A->C
        [2, 0, 1],   #B->A, B->B, B->C
        [5, 1, 0],   #C->A, C->B, C->C
    ]
    '''
    
    random.seed(42)
    n = int(input("Enter the number of vertices: "))
    V = generate_vertices(n)
    E_list = generate_adjacency_list(V, len(V), no_edge_prob=-1)
    E = adjacency_list_to_matrix(V, E_list)

    print("\nVertices: \n", V)
    print("Adjacency Matrix: ")
    for row in E:
        print(row)

    start_node = V[0]

    start_time = time.perf_counter()
    d, pi = dijkstra_matrix_array(V, E, start_node)
    end_time = time.perf_counter()
    time_taken = end_time - start_time
    print("\nDistances (d):")
    print(d)
    print("\nPredecessors (pi):")
    print(pi)
    print(f"\nTime taken: {time_taken:.9f} seconds")

if __name__ == "__main__":
    main()

