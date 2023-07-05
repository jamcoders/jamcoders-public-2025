# For answer checking without revealing the answer
def check_answers(answer, correct):
    if correct == answer:
        print("Your answer is correct!")
    else:
        print(f"Your answer: '{answer}' is wrong :( try again!")

def check_answers_with_num(answer, correct, num):
    if correct == answer:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")


def check_6_1a(ans):
    answer = "10 5"
    check_answers(ans, answer)

def check_6_1b(ans):
    answer = "0"
    check_answers(ans,answer)

def create_check_answer(correct, num):
    def check_fn(ans):
        check_answers_with_num(ans, correct, num)
    return check_fn

check_answer_3a = create_check_answer(3, '3a')
check_answer_3b = create_check_answer(3, '3b')
check_answer_3c = create_check_answer(3, '3c')
check_answer_3d = create_check_answer(1, '3d')
check_answer_4a = create_check_answer(9, '4a')
check_answer_4b = create_check_answer(3, '4b')
check_answer_6 = create_check_answer(25, '6')
