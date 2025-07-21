import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout


def add_edges(G, data):
  for word1 in data:
    for word2 in data[word1]:
      G.add_edge(word1, word2, weight=data[word1][word2])
  return G


def plot_graph():
    # Create a directed graph (tree)
    G = nx.DiGraph()

    # Add edges (with optional weights or labels)

    TOY_DATASET = {
        "<bos>": {"I": 1},
        "I": {"am": 0.5, "like": 0.5},
        "am": {"happy": 0.7, "sad": 0.2, "bananas": 0.1},
        "like": {"bananas": 0.6, "math": 0.4}
    }

    G = add_edges(G, TOY_DATASET)


    # Use graphviz layout with pydot (top-down)
    pos = graphviz_layout(G, prog='dot')  # 'dot' gives hierarchical top-down layout

    # Draw nodes and edges
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue',
            arrows=True, arrowstyle='->', arrowsize=20, font_size=12)

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title("Bigram Probabilities")
    plt.show()