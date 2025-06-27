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

check_answer_2_1 = create_check_answer(10, '2.1')
check_answer_2_2 = create_check_answer(6, '2.2')
check_answer_2_3 = create_check_answer(True, '2.3')
check_answer_2_4 = create_check_answer(True, '2.4')
check_answer_2_5 = create_check_answer(84, '2.5')
check_answer_2_6 = create_check_answer(24, '2.6')