#Code for part (a)

import time

def dijkstra_matrix_array(V, E, start):
    n_operations = 0
    n = len(V)
    idx = {V[i]: i for i in range(n)} #label -> index (e.g., "B" -> 1)
    dist = [float('inf')] * n #distance to infinity
    S = [False] * n #list of visted nodes
    parent = [-1] * n #predecessor index to reconstruct paths
    source = idx[start]
    dist[source] = 0 #start node to 0

    for _ in range(n):
        n_operations += 1
        u = -1 #u: current node
        best = float('inf')
        for i in range(n):
            n_operations += 1
            if not S[i] and dist[i] < best: #if not visited and the shortest distance
                best = dist[i] #replace best with shortest distance
                u = i
        if u == -1: #no more reachable vertices
            break

        S[u] = True #mark visited node as True

        row = E[u]
        for v in range(n):
            n_operations += 1
            w = row[v] #v: neighbouring node of u, w: weight of edge
            if S[v] or w == float('inf'):
                continue #skip if node visted or no edge
            alt = dist[u] + w
            n_operations += 1
            if alt < dist[v]: #check if alternate path is shorter than current best path
                dist[v] = alt
                parent[v] = u
                n_operations += 2

    d = {V[i]: dist[i] for i in range(n)}
    pi = {V[i]: (V[parent[i]] if parent[i] != -1 else None) for i in range(n)}

    return d, pi, n_operations

'''def main():
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
    current_time = time.time()
    d, pi = dijstra_matrix_array(V, E, "A")
    end_time = time.time()
    time_taken = end_time - current_time
    print(V)
    print(d)
    print(pi)
    print(time_taken)

if __name__ == "__main__":
    main()'''


#Code for part (b)

import heapq
import time

def dijkstra_list_heap(V, E, start):
    n_operations = 0
    d = {node: float('inf') for node in V} #distance to infinity
    pi = {node: None for node in V} #predecessor map to None
    S = set() #set of visted nodes
    d[start] = 0 #start node to 0

    pq = [(0, start)] #initialize priority queue

    while pq: #while priority queue not empty
        n_operations += 1
        dist_u, u = heapq.heappop(pq) #pop from priority queue, u: vetex with smallest distance
        if u in S: 
            continue
        S.add(u) #if unvisited, add to visited
        n_operations += 1
        for v, w in E.get(u, []): #v: neighbour of v, w: weight of edge connecting u to v
            n_operations += 1
            if v in S:
                continue
            alt = dist_u + w #alternate path
            if alt < d[v]:
                d[v] = alt
                pi[v]= u
                n_operations += 2
                heapq.heappush(pq, (alt, v)) #push new pair into priority queue
                n_operations += 1

    return d, pi, n_operations

'''def main():
    V = {"A", "B", "C"}
    E = {
        "A": [("B", 2), ("C", 5)],
        "B": [("A", 2), ("C", 1)],
        "C": [("A", 5), ("B", 1)]
    }
    current_time = time.time()
    d, pi = dijstra_list_heap(V, E, "A")
    end_time = time.time()
    time_taken = end_time - current_time
    print(V)
    print(d)
    print(pi)
    print(time_taken)'''

import random
import string

def generate_random_adj_list(num_vertices, num_edges, min_weight=1, max_weight=10):
    # Create vertex names as uppercase letters: 'A', 'B', 'C', ...
    V = [str(i) for i in range(num_vertices)]
    
    # All possible undirected edges (no self-loops)
    possible_edges = [(V[i], V[j]) for i in range(num_vertices) for j in range(i+1, num_vertices)]
    
    if num_edges > len(possible_edges):
        raise ValueError("Too many edges for the number of vertices.")
    
    # Randomly choose edges
    chosen_edges = random.sample(possible_edges, num_edges)
    
    # Build the adjacency dict
    E = {v: [] for v in V}
    for u, v in chosen_edges:
        weight = random.randint(min_weight, max_weight)
        E[u].append((v, weight))
        E[v].append((u, weight))  #undirected => add both ways
    
    return set(V), E

def adj_list_to_matrix(V, E):
    # Ensure V is a list for indexing
    if not isinstance(V, list):
        V = list(V)
    n = len(V)
    idx = {v: i for i, v in enumerate(V)}
    
    # Initialize n x n matrix with 0 (no edge)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for u in V:
        u_idx = idx[u]
        for v, w in E.get(u, []):
            v_idx = idx[v]
            matrix[u_idx][v_idx] = w
    
    return V, matrix



# Example usage:
# V, E = random_graph_dict(3, 3)
# print("V =", V)
# print("E =", E)

def main():
    #test 1: vary |V| for sparse and dense
    start_v_value = 5
    interval = 3

    #sparse
    for i in range(30):
        pass_num = i + 1
        gen_V, gen_E = generate_random_adj_list(start_v_value, start_v_value - 1)
        #part a
        print("Part (a) sparse graph pass {}:".format(pass_num))
        matrix_V, matrix_E = adj_list_to_matrix(gen_V, gen_E)
        current_time = time.time()
        a_v, a_e, a_n_operations = dijkstra_matrix_array(matrix_V, matrix_E, list(gen_V)[0])
        end_time = time.time()
        time_taken = end_time - current_time
        #print(a_v)
        #print(a_e)
        print("time taken,number of operations")
        print("{},{}".format(time_taken, a_n_operations))
        #part b
        print("Part (b) sparse graph pass {}:".format(pass_num))
        b_v, b_e, b_n_operations = dijkstra_list_heap(gen_V, gen_E, list(gen_V)[0])
        #print(b_v)
        #print(b_e)
        print("time taken,number of operations")
        print("{},{}".format(time_taken, b_n_operations))
        start_v_value += interval

    #dense
    for i in range(30):
        pass_num = i + 1
        gen_V, gen_E = generate_random_adj_list(start_v_value, (start_v_value * (start_v_value - 1))//2)
        #part a
        print("Part (a) dense graph pass {}:".format(pass_num))
        matrix_V, matrix_E = adj_list_to_matrix(gen_V, gen_E)
        current_time = time.time()
        a_v, a_e, a_n_operations = dijkstra_matrix_array(matrix_V, matrix_E, list(gen_V)[0])
        end_time = time.time()
        time_taken = end_time - current_time
        #print(a_v)
        #print(a_e)
        print("time taken,number of operations")
        print("{},{}".format(time_taken, a_n_operations))
        #part b
        print("Part (b) dense graph pass {}:".format(pass_num))
        current_time = time.time()
        b_v, b_e, b_n_operations = dijkstra_list_heap(gen_V, gen_E, list(gen_V)[0])
        end_time = time.time()
        time_taken = end_time - current_time
        #print(a_v)
        #print(a_e)
        print("time taken,number of operations")
        print("{},{}".format(time_taken, b_n_operations))
        start_v_value += interval

    #test 2: vary |E| with a fixed |V|
    fixed_v = 50
    min_e = 49
    max_e = (fixed_v * (fixed_v - 1)) // 2
    interval = (max_e - min_e) // 30
    e_val = min_e
    for i in range(30):
        pass_num = i + 1
        gen_V, gen_E = generate_random_adj_list(fixed_v, e_val)
        #part a
        print("Part (a) |V| = 50, |E| = {} graph pass {}:".format(e_val, pass_num))
        matrix_V, matrix_E = adj_list_to_matrix(gen_V, gen_E)
        current_time = time.time()
        a_v, a_e, a_n_operations = dijkstra_matrix_array(matrix_V, matrix_E, list(gen_V)[0])
        end_time = time.time()
        time_taken = end_time - current_time
        #print(a_v)
        #print(a_e)
        print("time taken,number of operations")
        print("{},{}".format(time_taken, a_n_operations))
        #part b
        print("Part (b) |V| = 50, |E| = {} graph pass {}:".format(e_val, pass_num))
        b_v, b_e, b_n_operations = dijkstra_list_heap(gen_V, gen_E, list(gen_V)[0])
        #print(b_v)
        #print(b_e)
        print("time taken,number of operations")
        print("{},{}".format(time_taken, b_n_operations))
        e_val += interval

if __name__ == "__main__":
    main()
