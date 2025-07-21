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
    # TODO arrows wider and thinner (proportional to probability)
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

# For answer checking without revealing the answer
def check_answers_with_num(answer, correct, num):
    if correct == answer:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")


def create_check_answer(correct, num):
    def check_fn(ans):
        check_answers_with_num(ans, correct, num)

    return check_fn


def check_answers_with_num_multi(answer, correct):
    if correct == answer:
        print(f"All your answers are correct!")
    else:
        print(f"At least one of your answers is wrong :( try again!")


def create_check_answer_multi(correct):
    def check_fn(ans):
        check_answers_with_num_multi(ans, correct)

    return check_fn


check_answer_1_1 = create_check_answer_multi(
    [8, 8, 3, False]
)
