import re
import pickle
import urllib.request
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# For answer checking without revealing the answer
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

# Fuzzy check for single numerical answer with tolerance
def check_answers_with_num_fuzzy(answer, correct, num, tol):
    if abs(answer - correct) <= tol:
        print(f"\033[92mYour answer to Question {num} is correct!\033[0m")
    else:
        print(f"\033[1;95mYour answer to Question {num}: '{answer}' is wrong :( try again!\033[0m")

def create_check_answer_fuzzy(correct, num, tol):
    def check_fn(ans):
        check_answers_with_num_fuzzy(ans, correct, num, tol)
    return check_fn

# Fuzzy check for multiple numerical answers with tolerances
def check_answers_with_num_multi_fuzzy(answer_list, correct_list, tolerances):
    all_correct = True
    for ans, correct, tol in zip(answer_list, correct_list, tolerances):
        if abs(ans - correct) > tol:
            all_correct = False
            break
    if all_correct:
        print(f"\033[92mAll your answers are correct!\033[0m")
    else:
        print(f"\033[1;95mAt least one of your answers is wrong :( try again!\033[0m")

def create_check_answer_multi_fuzzy(correct_list, tolerances):
    def check_fn(ans_list):
        check_answers_with_num_multi_fuzzy(ans_list, correct_list, tolerances)
    return check_fn

def clean(line):
    """
    Utility function for NLP project.

    Clean up a line of text by:
    - Replacing ellipses with single periods
    - Removing quotes
    - Removing tabs
    - Make text lowercase
    - Smush standalone apostrophes with surrounding words

    Args:
        line (str): Input string to clean

    Returns:
        str: Cleaned string
    """
    line = line.replace("...", ".")
    line = line.replace("….", ".")
    line = line.replace("\t", " ")
    line = line.replace('"', "")
    line = line.replace("`", "'")
    line = line.replace("’", "'")
    line = re.sub(r"\s'\s", "'", line)
    line = " ".join(line.split())
    line = line.lower()
    return line

def load_dataset():
    url = "https://raw.githubusercontent.com/jamcoders/jamcoders-public-2025/main/jamcoders/week4/data/corpus.pkl"
    with urllib.request.urlopen(url) as response:
        corpus = pickle.load(response)
    return corpus

def plot_wordcloud(word_counts):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def visualize_barplot(word_data, top_n: int = 15) -> None:
    """
    Visualize word distribution as a bar chart.
    
    Args:
        word_data: Dictionary mapping words to counts or probabilities
        top_n: Number of top words to display
    """
    total = sum(word_data.values())
    if total > 1.1:
        word_probs = {word: count/total for word, count in word_data.items()}
    else:
        word_probs = word_data
    top_words = sorted(word_probs.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words, probs = zip(*top_words)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(range(len(words)), probs)
    plt.xticks(range(len(words)), words, rotation=45, ha='right')
    plt.ylabel('Probability')
    plt.title(f'Top {top_n} Words by Frequency')
    plt.tight_layout()
    for bar, prob in zip(bars, probs):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height, f'{prob:.3f}', ha='center', va='bottom', fontsize=8)
    plt.show()

check_answer_1_6 = create_check_answer_multi_fuzzy(
    [19790, 93.51258755002858], [1000, 5]
)
check_answer_3_1 = create_check_answer_multi(
    [["you", "dogs"], 0.4, "you", ["i", "love", "you", "so", "much"]]
)
