import requests
import matplotlib.pyplot as plt

def get_harry_potter_data():
    url = "https://dgoldberg.sdsu.edu/515/harrypotter.txt"
    response = requests.get(url)
    
    if response.status_code == 200:
        text = response.text
    else:
        print(f"Failed to fetch file: {response.status_code}")
        return
    
    sentences = text.replace("Mr.", "Mr").replace("Mrs.", "Mrs").replace("?",".").replace("!",".").split('.')
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
    plt.ylabel('Number of Co-Ocurrences')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
