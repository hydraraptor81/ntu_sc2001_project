"""
SC2001 Project 2 Dijkstra algorithm
Authors: Aw Hwee Ren, Eamon Ching Yupeng, Ethan Jared Chong Rui Zhi
Date: 2025-10-11
"""

import time
import random
import string
import heapq
from visualize import visualize_graph

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

def generate_random_adj_list(num_vertices, num_edges, min_weight=1, max_weight=10):
    if num_edges < num_vertices-1:
        raise ValueError("Not enough edges for a connected graph.")

    V = [f"V{i}" for i in range(num_vertices)]
    # All possible undirected edges (no self-loops)
    possible_edges = [(V[i], V[j]) for i in range(num_vertices) for j in range(i+1, num_vertices)]
    
    if num_edges > (num_vertices * (num_vertices-1) // 2):
        raise ValueError("Too many edges for the number of vertices.")
    
    vertices = list(range(num_vertices))
    random.shuffle(vertices)
    tree_edges = []
    for i in range(0, num_vertices-1):
        u, v = vertices[i], vertices[i+1]
        tree_edges.append((V[u], V[v]))

    remaining = num_edges - (num_vertices-1)
    other_possible_edges = [e for e in possible_edges if e not in tree_edges]
    if remaining > len(other_possible_edges):
        raise ValueError("Too many edges")

    # Randomly fill remaining edges
    extra_edges = random.sample(other_possible_edges, remaining)
    all_edges = tree_edges + extra_edges
    
    # Build the adjacency dict
    E = {v: [] for v in V}
    for u, v in all_edges:
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
    matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    for u in V:
        u_idx = idx[u]
        for v, w in E.get(u, []):
            v_idx = idx[v]
            matrix[u_idx][v_idx] = w
    
    return V, matrix

def main():
    v_value = 0
    interval = 10
    n_points = 10
    n_iterations = 30
    #test 1: vary |V| for sparse and dense
    print("Varying |V| for sparse and dense graphs")
    #sparse
    print("=====Start of sparse======")
    for n in range(n_points):
        total_a_time = 0
        total_b_time = 0
        average_a_time = 0
        average_b_time = 0
        total_a_operations = 0
        total_b_operations = 0
        v_value += interval
        for i in range(n_iterations):
            V, E = generate_random_adj_list(v_value, v_value - 1)
            #visualize_graph(V, E)
            #part a
            matrix_V, matrix_E = adj_list_to_matrix(V, E)
            current_time = time.perf_counter()
            a_v, a_e, a_operations = dijkstra_matrix_array(matrix_V, matrix_E, list(V)[0])
            end_time = time.perf_counter()
            time_taken = end_time - current_time
            total_a_time += time_taken
            total_a_operations += a_operations
            #part b
            current_time = time.perf_counter()
            b_v, b_e, b_operations = dijkstra_list_heap(V, E, list(V)[0])
            end_time = time.perf_counter()
            time_taken = end_time - current_time
            total_b_time += time_taken
            total_b_operations += b_operations
        
        average_a_time = total_a_time / n_iterations
        average_b_time = total_b_time / n_iterations
        average_a_operations = total_a_operations / n_iterations
        average_b_operations = total_b_operations / n_iterations
        print("Part a")
        print(f"For sparse graph of |V|={v_value}, using adjacency matrix, with array priority queue")
        print(f"Average time taken {average_a_time}s")
        print(f"Average number of operations {average_a_operations}\n")
        print("Part b")
        print(f"For sparse graph of |V|={v_value}, using adjacency list, with min-heap priority queue")
        print(f"Average Time taken {average_b_time}s")
        print(f"Average number of operations {average_b_operations}\n")
    print("=====End of sparse======")
    #dense
    print("=====Start of dense======")
    v_value = 0
    for n in range(n_points):
        total_a_time = 0
        total_b_time = 0
        average_a_time = 0
        average_b_time = 0
        total_a_operations = 0
        total_b_operations = 0
        v_value += interval
        for i in range(n_iterations):
            V, E = generate_random_adj_list(v_value, (v_value * (v_value - 1))//2)
#        visualize_graph(V, E)
            #part a
            matrix_V, matrix_E = adj_list_to_matrix(V, E)
            current_time = time.perf_counter()
            a_v, a_e, a_operations = dijkstra_matrix_array(matrix_V, matrix_E, list(V)[0])
            end_time = time.perf_counter()
            time_taken = end_time - current_time
            total_a_time += time_taken
            total_a_operations += a_operations
            #part b
            current_time = time.perf_counter()
            b_v, b_e, b_operations = dijkstra_list_heap(V, E, list(V)[0])
            end_time = time.perf_counter()
            time_taken = end_time - current_time
            total_b_time += time_taken
            total_b_operations += b_operations

        average_a_time = total_a_time / n_iterations
        average_b_time = total_b_time / n_iterations
        average_a_operations = total_a_operations / n_iterations
        average_b_operations = total_b_operations / n_iterations
        print("Part a")
        print(f"For dense graph of |V|={v_value}, using adjacency matrix, with array priority queue")
        print(f"Average time taken {average_a_time}s")
        print(f"Average number of operations {average_a_operations}\n")
        print("Part b")
        print(f"For dense graph of |V|={v_value}, using adjacency list, with min-heap priority queue")
        print(f"Average Time taken {average_b_time}s")
        print(f"Average number of operations {average_b_operations}\n")

    print("=====End of dense======")
    #test 2: vary |E| with a fixed |V|
    fixed_v = 100
    min_e = fixed_v - 1
    max_e = (fixed_v * (fixed_v - 1)) // 2
    interval = (max_e - min_e) // (n_points-1)
    e_val = 0
    print("Varying |E| given fixed |V|")
    for n in range(n_points):
        total_a_time = 0
        total_b_time = 0
        average_a_time = 0
        average_b_time = 0
        total_a_operations = 0
        total_b_operations = 0
        if n == (n_points-1):
            e_val = max_e           
        else:
            e_val = min_e + n * interval
        for i in range(n_iterations):
            V, E = generate_random_adj_list(fixed_v, e_val)
            #visualize_graph(V, E)
            #part a
            matrix_V, matrix_E = adj_list_to_matrix(V, E)
            current_time = time.perf_counter()
            a_v, a_e, a_operations = dijkstra_matrix_array(matrix_V, matrix_E, list(V)[0])
            end_time = time.perf_counter()
            time_taken = end_time - current_time
            total_a_time += time_taken
            total_a_operations += a_operations
            #part b
            current_time = time.perf_counter()
            b_v, b_e, b_operations = dijkstra_list_heap(V, E, list(V)[0])
            end_time = time.perf_counter()
            time_taken = end_time - current_time
            total_b_time += time_taken
            total_b_operations += b_operations
        
        average_a_time = total_a_time / n_iterations
        average_b_time = total_b_time / n_iterations
        average_a_operations = total_a_operations / n_iterations
        average_b_operations = total_b_operations / n_iterations
        print("Part a")
        print(f"For dense graph of fixed |V|={fixed_v} and |E|={e_val}, using adjacency matrix, with array priority queue")
        print(f"Average time taken {average_a_time}s")
        print(f"Average number of operations {average_a_operations}\n")
        print("Part b")
        print(f"For dense graph of fixed |V|={fixed_v} and |E|={e_val}, using adjacency list, with min-heap priority queue")
        print(f"Average Time taken {average_b_time}s")
        print(f"Average number of operations {average_b_operations}\n")

if __name__ == "__main__":
    main()
