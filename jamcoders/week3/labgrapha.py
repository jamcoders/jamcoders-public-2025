# For answer checking without revealing the answer
def check_answers(answer, correct, subset=False):
    if subset and (answer in correct):
            print(f"Your answer is correct!")
    elif correct == answer:
        print(f"Your answer is correct!")
    else:
        print(f"Your answer: '{answer}' is wrong :( try again!")


def create_check_answer(correct, subset=False):
    def check_fn(ans):
        check_answers(ans, correct, subset)
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


check_answer_1_1 = create_check_answer({0,1,2,3,4}, True)
check_answer_1_2 = create_check_answer({(0, 1), (0, 2), (2, 3), (3, 4), (2, 4), (0, 4),
                                       (1, 0), (2, 0), (3, 2), (4, 3), (4, 2), (4, 0)}, True)
check_answer_1_3 = create_check_answer(6)
check_answer_1_4 = create_check_answer(5)
check_answer_2_2 = create_check_answer({3,4}, True)
check_answer_2_3 = create_check_answer(3)
check_answer_2_4 = create_check_answer(0)
check_answer_2_5 = create_check_answer([[2,3,4,2], [3,4,2,3], [4,2,3,4], [4,3,2,4], [2,4,3,2,], [3,2,4,3], [0,3,4,0], [0,4,3,0], [3,0,4,3], [3,4,0,3], [4,0,3,4], [4,3,0,4]], True)
check_answer_3_2 = create_check_answer_multi([False,False,True])
check_answer_3_3 = create_check_answer_multi([True,True,False])
