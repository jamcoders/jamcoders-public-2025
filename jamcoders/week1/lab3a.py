# For answer checking without revealing the answer
def check_answers(answer, correct):
    if correct == answer:
        print("Your answer is correct!")
    else:
        print(f"Your answer: '{answer}' is wrong :( try again!")


def check_7_1a(ans):
    answer = "10 5"
    check_answers(ans, answer)

def check_7_1b(ans):
    answer = "0"
    check_answers(ans,answer)