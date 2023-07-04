# For answer checking without revealing the answer
def check_answers(answer, correct):
    if correct == answer:
        print("Your answer is correct!")
    else:
        print(f"Your answer: '{answer}' is wrong :( try again!")


def answer_true(ans):
    answer = True
    check_answers(ans, answer)

def answer_false(ans):
    answer = False
    check_answers(ans, answer)

def check_answer1(ans): answer_false(ans)
def check_answer2(ans): answer_false(ans)
def check_answer3(ans): answer_true(ans)
def check_answer4(ans): answer_true(ans)
def check_answer5(ans): answer_true(ans)
def check_answer6(ans): answer_false(ans)
def check_answer7(ans): answer_true(ans)
def check_answer8(ans): answer_true(ans)
