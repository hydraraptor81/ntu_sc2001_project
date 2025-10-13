# visualize.py

import networkx as nx
import matplotlib.pyplot as plt
import os

def visualize_graph(V, E, filename="graph.png", folder="graphs", iteration=None, graph_type="sparse"):
    """
    Visualizes an undirected graph using NetworkX and Matplotlib, saving to a file.

    Args:
    - V: Set or list of vertices (e.g., {'V0', 'V1', ...}).
    - E: Adjacency list (dict) where keys are vertices and values are lists of (neighbor, weight) tuples.
    - filename: Name of the file to save the visualization.
    - folder: Base directory to save the visualization (default: "graphs").
    - iteration: Optional iteration number for labeling and subfolder creation.
    - graph_type: Type of graph ("sparse", "dense", or "fixed_v") for subfolder organization.
    """

    # Create base folder if not exists
    os.makedirs(folder, exist_ok=True)

    # Create subfolder structure: graphs/sparse/trial_0/, graphs/sparse/trial_1/, etc.
    if iteration is not None:
        subfolder = os.path.join(folder, graph_type, f"trial_{iteration}")
    else:
        subfolder = os.path.join(folder, graph_type)

    os.makedirs(subfolder, exist_ok=True)

    G = nx.Graph()  # Undirected graph
    G.add_nodes_from(V)
    for u in E:
        for v, w in E[u]:
            G.add_edge(u, v, weight=w)

    # Calculate |V| and |E|
    num_vertices = len(V)
    num_edges = G.number_of_edges()

    # Determine if the graph is sparse or dense
    max_possible_edges = num_vertices * (num_vertices - 1) // 2
    if max_possible_edges == 0:
        density_label = "N/A"
    else:
        density = num_edges / max_possible_edges
        density_label = "dense" if density > 0.5 else "sparse"

    # Create title with all required information
    title_parts = [
        f"Graph Visualization",
        f"|V|={num_vertices}",
        f"|E|={num_edges}",
        f"{density_label}"
    ]
    if iteration is not None:
        title_parts.append(f"Iteration {iteration}")
    title = " ".join(title_parts)

    # Draw the graph
    plt.figure(figsize=(10, 8))  
    pos = nx.spring_layout(G, seed=42)  

    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=700, font_size=10, font_weight='bold')

    # Draw edge labels if weights are not all 1
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    if not all(w == 1 for w in edge_labels.values()):
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(title)

    filepath = os.path.join(subfolder, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()  

    print(f"Graph visualization saved to {filepath}")

