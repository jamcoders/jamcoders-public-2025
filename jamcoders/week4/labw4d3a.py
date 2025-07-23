import requests
import matplotlib.pyplot as plt
import networkx as nx


def get_harry_potter_data():
    url = "https://dgoldberg.sdsu.edu/515/harrypotter.txt"
    response = requests.get(url)
    
    if response.status_code == 200:
        text = response.text
    else:
        print(f"Failed to fetch file: {response.status_code}")
        return
    
    sentences = text.replace("Mr.", "Mr").replace("Mrs.", "Mrs").replace("\n","").replace("\r","").replace("? ",". ").replace("! ",". ").split('. ')
    return sentences

def visualize_bar_chart(co_occurrence_data):
    sorted_items = sorted(co_occurrence_data.items(), key=lambda x: x[1], reverse=True)
    # Unpack keys and values
    labels, values = zip(*sorted_items)
    labels = [label[0] + ' - ' + label[1] for label in labels]
    # Plot
    plt.figure(figsize=(15, 8))
    plt.bar(labels, values, color='skyblue')
    plt.title('Character Co-Occurrences')
    plt.xlabel('Character Pairings')
    plt.ylabel('Number of Co-Occurrences')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def visualize_cooccurence(G, k, weighted=True):
  pos = nx.spring_layout(G, weight='weight', k=k, seed=0)  # weight controls layout distance
  if weighted:
    edge_widths = [G[u][v]['weight']/10 for u, v in G.edges()]
    title = "Character Co-occurrence Graph"
  else:
    edge_widths = [G[u][v]['weight'] for u, v in G.edges()]
    title = "Unweighted Character Co-occurrence Graph"

  plt.figure(figsize=(8, 6))
  nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    width=edge_widths,  # This controls edge thickness
    edge_color='gray'
  )

  plt.title(title)
  plt.show()
