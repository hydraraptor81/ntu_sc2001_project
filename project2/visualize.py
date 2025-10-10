import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(V, E):
    """
    Visualizes an undirected graph using NetworkX and Matplotlib.

    Args:
    - V: Set or list of vertices (e.g., {'V0', 'V1', ...}).
    - E: Adjacency list (dict) where keys are vertices and values are lists of (neighbor, weight) tuples.
    """
    G = nx.Graph()  # Undirected graph
    G.add_nodes_from(V)
    for u in E:
        for v, w in E[u]:
            G.add_edge(u, v, weight=w)

    # Draw the graph
    plt.figure(figsize=(8, 6))  # Adjust size as needed
    pos = nx.spring_layout(G)  # Positions for nodes (spring layout for aesthetics)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    plt.title(f"Graph Visualization (|V|={len(V)}, |E|={G.number_of_edges()})")
    plt.show()

