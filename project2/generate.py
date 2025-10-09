#generate.py
import random

def generate_vertices(n):
    return [f"V{i}" for i in range(n)]

def generate_adjacency_list(V, n, max_weight=10, no_edge_prob=-1):
    E = {v: [] for v in V}
    V_list = list(V)

    ''' example, 0->1, unidirectional, not reversible, 1->0 is not generated
    (0,0) (0,1) (0,2)
          (1,1) (1,2) 
                (2,2)
    '''

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < no_edge_prob:
                continue
            u, v = V_list[i], V_list[j]
            weight = random.randint(1, max_weight)
            if random.choice([True, False]):
                E[u].append((v, weight))  # u -> v
            else:
                E[v].append((u, weight))  # v -> u
    return E

def adjacency_list_to_matrix(V, E_list):
    n = len(V)
    E_matrix = [[float('inf')] * n for _ in range(n)]
    idx = {v: i for i, v in enumerate(V)}

    for u in E_list:
        i = idx[u]
        E_matrix[i][i] = 0
        for v, w in E_list[u]:
            j = idx[v]
            E_matrix[i][j] = w

    return E_matrix
