"""
SC2001 Project 2 Dijkstra algorithm
Authors: Aw Hwee Ren, Eamon Ching Yupeng, Ethan Jared Chong Rui Zhi
Date: 2025-10-11
"""

import time
import random
import heapq
from visualize import visualize_graph
from visualize_dijkstra import plot_dijkstra_comparison
#from save_results import save_results

def dijkstra_matrix_array(V, E, start):
    n_operations = 0
    n = len(V)
    idx = {V[i]: i for i in range(n)}   #label -> index (e.g., "B" -> 1)
    dist = [float('inf')] * n           #distance to infinity
    S = [False] * n                     #list of visited nodes
    parent = [-1] * n                   #predecessor index to reconstruct paths
    source = idx[start]
    dist[source] = 0                    #start node to 0

    for _ in range(n):
        n_operations += 1
        u = -1                          #u: current node
        best = float('inf')
        for i in range(n):
            n_operations += 1
            if not S[i] and dist[i] < best: #if not visited and the shortest distance
                best = dist[i]              #replace best with shortest distance
                u = i
        if u == -1:                         #no more reachable vertices
            break

        S[u] = True                     #mark visited node as True

        row = E[u]
        for v in range(n):
            n_operations += 1
            w = row[v]                  #v: neighbouring node of u, w: weight of edge
            if S[v] or w == float('inf'):
                continue                #skip if node visited or no edge
            alt = dist[u] + w
            n_operations += 1
            if alt < dist[v]:           #check if alternate path is shorter than current best path
                dist[v] = alt
                parent[v] = u
                n_operations += 2

    d = {V[i]: dist[i] for i in range(n)}
    pi = {V[i]: (V[parent[i]] if parent[i] != -1 else None) for i in range(n)}

    return d, pi, n_operations

def dijkstra_list_heap(V, E, start):
    n_operations = 0
    d = {node: float('inf') for node in V}  #distance to infinity
    pi = {node: None for node in V}         #predecessor map to None
    S = set()                               #set of visited nodes
    d[start] = 0                            #start node to 0

    pq = [(0, start)]                       #initialize priority queue

    while pq:                               #while priority queue not empty
        n_operations += 1
        dist_u, u = heapq.heappop(pq)       #pop from priority queue, u: vertex with smallest distance
        if u in S: 
            continue
        S.add(u)                            #if unvisited, add to visited
        n_operations += 1
        for v, w in E.get(u, []):           #v: neighbour of v, w: weight of edge connecting u to v
            n_operations += 1
            if v in S:
                continue
            alt = dist_u + w                #alternate path
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

    if num_edges > (num_vertices * (num_vertices-1) // 2):
        raise ValueError("Too many edges for the number of vertices.")

    # Generate all possible edges
    all_possible_edges = []
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            all_possible_edges.append((V[i], V[j]))

    random.shuffle(all_possible_edges)
    selected_edges = set()

    # Create spanning tree
    vertices = list(range(num_vertices))
    random.shuffle(vertices)
    for i in range(num_vertices - 1):
        u, v = vertices[i], vertices[i+1]
        if u > v:
            u, v = v, u
        selected_edges.add((V[u], V[v]))

    # Add remaining edges
    for edge in all_possible_edges:
        if len(selected_edges) >= num_edges:
            break
        selected_edges.add(edge)

    # Build adjacency list
    E = {v: [] for v in V}
    for u, v in selected_edges:
        weight = random.randint(min_weight, max_weight)
        E[u].append((v, weight))
        E[v].append((u, weight))                        # undirected

    return V, E

def adj_list_to_matrix(V, E):
    # Ensure V is a list for indexing
    if not isinstance(V, list):
        V = list(V)
    n = len(V)
    idx = {v: i for i, v in enumerate(V)}

    # Initialize n x n matrix with infinity (no edge)
    matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

    for u in V:
        u_idx = idx[u]
        for v, w in E.get(u, []):
            v_idx = idx[v]
            matrix[u_idx][v_idx] = w

    return V, matrix

def run_algorithm_comparison(V, E, graph_type, v_value, e_value, n_iterations):
    total_a_time = 0
    total_b_time = 0
    total_a_operations = 0
    total_b_operations = 0

    for trial in range(n_iterations):
        # Generate a new random graph for each iteration
        if graph_type != "fixed_v":
            V, E = generate_random_adj_list(v_value, e_value)
        # After generating V, E
#            visualize_graph(V, E, f"V{v_value}_{graph_type}_n{trial}.png", iteration=trial, graph_type=graph_type)
#        else:
#            visualize_graph(V, E, f"E{e_value}_{graph_type}_n{trial}.png", iteration=trial, graph_type=graph_type)
        # initialize starting
        start_node = list(V)[0]

        # Run both versions of Dijkstra
        matrix_V, matrix_E = adj_list_to_matrix(V, E)
        current_time = time.perf_counter()
        a_distances, a_predecessors, a_operations = dijkstra_matrix_array(matrix_V, matrix_E, start_node)
        end_time = time.perf_counter()
        trial_a_time = end_time - current_time
        total_a_time += trial_a_time
        total_a_operations += a_operations

        current_time = time.perf_counter()
        b_distances, b_predecessors, b_operations = dijkstra_list_heap(V, E, start_node)
        end_time = time.perf_counter()
        trial_b_time = end_time - current_time
        total_b_time += trial_b_time
        total_b_operations += b_operations
    '''
        save_results(
            trial=trial,
            v_value=v_value,
            e_value=e_value,
            graph_type=graph_type,
            V=V,
            E=E,
            matrix_V=matrix_V,
            matrix_E=matrix_E,
            start_node=start_node,
            a_distances=a_distances,
            a_predecessors=a_predecessors,
            a_operations=a_operations,
            matrix_time=trial_a_time,
            b_distances=b_distances,
            b_predecessors=b_predecessors,
            b_operations=b_operations,
            heap_time=trial_b_time
        )
    '''
    # Compute averages
    avg_a_time = total_a_time / n_iterations
    avg_b_time = total_b_time / n_iterations
    avg_a_ops = total_a_operations / n_iterations
    avg_b_ops = total_b_operations / n_iterations

    return avg_a_time, avg_b_time, avg_a_ops, avg_b_ops

def main(n_points=10, n_iterations=2, v_interval=1000):
    results = []

    print("Varying |V| for sparse and dense graphs")

    # Sparse graphs
    print("=====Start of sparse======")
    v_value = 0
    for n in range(n_points):
        v_value += v_interval


        # For sparse graphs, e_value = v_value - 1
        avg_a_time, avg_b_time, avg_a_ops, avg_b_ops = run_algorithm_comparison(
            V=None, E=None, graph_type="sparse", 
            v_value=v_value, e_value=v_value - 1, 
            n_iterations=n_iterations
        )

        graph_desc = f"sparse graph of |V|={v_value}"
        print("Part a")
        print(f"For {graph_desc}, using adjacency matrix, with array priority queue")
        print(f"Average time taken {avg_a_time:.9f}s")
        print(f"Average number of operations {avg_a_ops:.2f}\n")
        print("Part b")
        print(f"For {graph_desc}, using adjacency list, with min-heap priority queue")
        print(f"Average Time taken {avg_b_time:.9f}s")
        print(f"Average number of operations {avg_b_ops:.2f}\n")

        result = {
            'type': 'sparse',
            'v_count': v_value,
            'e_count': v_value - 1,
            'matrix_avg_time': avg_a_time,
            'heap_avg_time': avg_b_time,
            'matrix_avg_operations': avg_a_ops,
            'heap_avg_operations': avg_b_ops
        }
        results.append(result)

    print("=====End of sparse======")

    # Dense graphs
    print("=====Start of dense======")
    v_value = 0
    for n in range(n_points):
        v_value += v_interval
        num_edges = (v_value * (v_value - 1)) // 2
        avg_a_time, avg_b_time, avg_a_ops, avg_b_ops = run_algorithm_comparison(
            V=None, E=None, graph_type="dense", 
            v_value=v_value, e_value=num_edges, 
            n_iterations=n_iterations
        )

        graph_desc = f"dense graph of |V|={v_value}"
        print("Part a")
        print(f"For {graph_desc}, using adjacency matrix, with array priority queue")
        print(f"Average time taken {avg_a_time:.9f}s")
        print(f"Average number of operations {avg_a_ops:.2f}\n")
        print("Part b")
        print(f"For {graph_desc}, using adjacency list, with min-heap priority queue")
        print(f"Average Time taken {avg_b_time:.9f}s")
        print(f"Average number of operations {avg_b_ops:.2f}\n")

        result = {
            'type': 'dense',
            'v_count': v_value,
            'e_count': num_edges,
            'matrix_avg_time': avg_a_time,
            'heap_avg_time': avg_b_time,
            'matrix_avg_operations': avg_a_ops,
            'heap_avg_operations': avg_b_ops
        }
        results.append(result)

    print("=====End of dense======")

    # Vary |E| with fixed |V|
    fixed_v = 10000
    min_e = fixed_v - 1
    max_e = (fixed_v * (fixed_v - 1)) // 2
    interval_e = (max_e - min_e) // (n_points - 1) if n_points > 1 else 0
    print("Varying |E| given fixed |V|")

    for n in range(n_points):
        if n == (n_points - 1):
            e_val = max_e
        else:
            e_val = min_e + n * interval_e

        # For fixed_v graphs, we need to generate V and E once
        V, E = generate_random_adj_list(fixed_v, e_val)
        avg_a_time, avg_b_time, avg_a_ops, avg_b_ops = run_algorithm_comparison(
            V=V, E=E, graph_type="fixed_v", 
            v_value=fixed_v, e_value=e_val, 
            n_iterations=n_iterations
        )

        graph_desc = f"graph of fixed |V|={fixed_v} and |E|={e_val}"
        print("Part a")
        print(f"For {graph_desc}, using adjacency matrix, with array priority queue")
        print(f"Average time taken {avg_a_time:.9f}s")
        print(f"Average number of operations {avg_a_ops:.2f}\n")
        print("Part b")
        print(f"For {graph_desc}, using adjacency list, with min-heap priority queue")
        print(f"Average Time taken {avg_b_time:.9f}s")
        print(f"Average number of operations {avg_b_ops:.2f}\n")

        result = {
            'type': 'fixed_v',
            'v_count': fixed_v,
            'e_count': e_val,
            'matrix_avg_time': avg_a_time,
            'heap_avg_time': avg_b_time,
            'matrix_avg_operations': avg_a_ops,
            'heap_avg_operations': avg_b_ops
        }
        results.append(result)

    # Generate plots
    plot_dijkstra_comparison(results)

    return results

if __name__ == "__main__":
    main()

