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

check_answer_3_1a = create_check_answer('10 5', '3.1 (a)')
check_answer_3_1b = create_check_answer('0', '3.1 (b)')
