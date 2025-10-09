import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(V, E):
    G = nx.DiGraph()  # Use DiGraph for directed graph
    for i in range(len(V)):
        for j in range(len(V)):
            if E[i][j] != float('inf') and E[i][j] != 0:
                G.add_edge(V[i], V[j], weight=E[i][j])

    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("Graph Visualization")
    plt.show()


