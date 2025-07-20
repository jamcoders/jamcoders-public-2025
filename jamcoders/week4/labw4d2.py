import re


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


# Fuzzy check for single numerical answer with tolerance
def check_answers_with_num_fuzzy(answer, correct, num, tol):
    if abs(answer - correct) <= tol:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")


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
        print(f"All your answers are correct!")
    else:
        print(f"At least one of your answers is wrong :( try again!")


def create_check_answer_multi_fuzzy(correct_list, tolerances):
    def check_fn(ans_list):
        check_answers_with_num_multi_fuzzy(ans_list, correct_list, tolerances)

    return check_fn


def clean(line):
    """
    Utility functon for NLP project.

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

    # Replace ellipses (...) with single period
    line = line.replace("...", ".")
    line = line.replace("….", ".")  # Handle other ellipsis variations

    # Remove tabs
    line = line.replace("\t", " ")

    # Remove quote
    line = line.replace('"', "")
    line = line.replace("`", "'")
    line = line.replace("’", "'")

    # Smush standalone apostrophes:
    # For example: convert "word ' word" to "word'word"
    # Use regex to replace occurrences of space + apostrophe + space with just apostrophe
    line = re.sub(r"\s'\s", "'", line)

    # Clean up multiple spaces again (because we replaced tabs and smushed apostrophes)
    line = " ".join(line.split())

    # Lowercase
    line = line.lower()

    return line


check_answer_1_4 = create_check_answer_multi_fuzzy(
    [19790, 93.51258755002858], [1000, 5]
)
check_answer_3_1 = create_check_answer_multi(
    [["you", "dogs"], 0.4, "you", ["i", "love", "you", "so", "much"]]
)
