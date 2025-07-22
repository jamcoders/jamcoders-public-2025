import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
import random

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
    pos = graphviz_layout(G, prog="dot")
    edge_weights = [G[u][v]["weight"] * 5 for u, v in G.edges()]
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
        width=edge_weights,
    )
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    plt.title("Bigram Probabilities")
    plt.show()

# For answer checking with color
def check_answers_with_num(answer, correct, num):
    if correct == answer:
        print(f"\033[92mYour answer to Question {num} is correct!\033[0m")
    else:
        print(f"\033[1;95mYour answer to Question {num}: '{answer}' is wrong :( try again!\033[0m")

def create_check_answer(correct, num):
    def check_fn(ans):
        check_answers_with_num(ans, correct, num)
    return check_fn

def check_answers_with_num_multi(answer, correct):
    if correct == answer:
        print(f"\033[92mAll your answers are correct!\033[0m")
    else:
        print(f"\033[1;95mAt least one of your answers is wrong :( try again!\033[0m")

def create_check_answer_multi(correct):
    def check_fn(ans):
        check_answers_with_num_multi(ans, correct)
    return check_fn

def sample_from_dict(prob_dict):
    """
    Sample an item from a dictionary of probabilities.

    Args:
        prob_dict: Dictionary mapping items to their probabilities.
                   Probabilities should sum to 1.

    Returns:
        A randomly sampled key from the dictionary, weighted by probabilities.
    """
    assert isinstance(prob_dict, dict), "Input must be a dictionary"
    assert len(prob_dict) > 0, "Input must not be empty"
    assert all(isinstance(k, str) for k in prob_dict.keys()), "Keys must be strings"
    for v in prob_dict.values():
        assert isinstance(v, float), "Probabilities must be floats"
        assert 0 <= v <= 1, "Probabilities must be between 0 and 1"
    assert abs(sum(prob_dict.values()) - 1) < 1e-6, "Probabilities must sum to 1"

    r = random.random()
    cumulative = 0

    for item, prob in prob_dict.items():
        cumulative += prob
        if r <= cumulative:
            return item
    raise ValueError(
        "Probabilities do not sum to 1")  # Could this happen due to floating point error? Lmk if you see this!

check_answer_1_1 = create_check_answer_multi(
    [8, 8, 3, False]
)