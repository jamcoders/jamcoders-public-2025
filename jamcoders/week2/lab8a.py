# For answer checking without revealing the answer
def check_answers(answer, correct, num):
    if correct == answer:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")


def check_answer1(a):
    check_answers(a, -27, "1.1")

def check_answer2(a, b, c):
    check_answers([a, b, c], ["a", "1", "x is not in L"], "1.2")

def check_answer3(a, b, c, d):
    check_answers([a, b, c, d], ["x is not in L", "x is in L", 9002, 2000], "1.3")

def check_answer4(a, b, c, d, e):
    check_answers([a, b, c, d, e], [5, 17, 14, 9, 120], "1.4")