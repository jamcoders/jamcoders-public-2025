import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout


def generate_graph(weighted_adj_list):
    G = nx.DiGraph()
    G = add_edges(G, weighted_adj_list)
    return G


def add_edges(G, data):
    for word1 in data:
        for word2 in data[word1]:
            G.add_edge(word1, word2, weight=data[word1][word2])
    return G


def plot_graph(G):
    # Use graphviz layout with pydot (top-down)
    pos = graphviz_layout(G, prog="dot")  # 'dot' gives hierarchical top-down layout

    # Draw nodes and edges
    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="lightblue",
        arrows=True,
        arrowstyle="->",
        arrowsize=20,
        font_size=12,
    )

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title("Bigram Probabilities")
    plt.show()
