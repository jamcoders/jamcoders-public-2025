# For answer checking without revealing the answer
def check_answers(answer, correct):
    if correct == answer:
        print("Your answer is correct!")
    else:
        print(f"Your answer: '{answer}' is wrong :( try again!")


def check_1a(ans):
    answer = "global variables"
    check_answers(ans, answer)

def check_1b(ans):
    answer = "local variables"
    check_answers(ans,answer)