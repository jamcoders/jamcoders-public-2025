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

check_answer_2_1a = create_check_answer(10, '2.1a')
check_answer_2_1b = create_check_answer(14, '2.1b')
check_answer_2_1c_1 = create_check_answer(False, '2.1c_1')
check_answer_2_1c_2 = create_check_answer(14, '2.1c_2')
check_answer_2_1d_1 = create_check_answer(True, '2.1d_1')
check_answer_2_1d_2 = create_check_answer(13, '2.1d_2')