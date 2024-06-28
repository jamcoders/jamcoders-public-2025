# For answer checking without revealing the answer
def check_answers_with_num(answer, correct):
    if correct == answer:
        print(f"Your answer is correct!")
    else:
        print(f"Your answer: '{answer}' is wrong :( try again!")


def create_check_answer(correct):
    def check_fn(ans):
        check_answers_with_num(ans, correct)
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


check_answer_1_0 = create_check_answer_multi([False,False,True,True,True,True,False])
check_answer_2_1 = create_check_answer(337*(337-1) // 2)
check_answer_2_2 = create_check_answer(337*(337-1))