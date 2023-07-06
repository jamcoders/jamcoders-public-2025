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

def check_answers_with_num_multi(answer, correct):
    if correct == answer:
        print(f"All your answers are correct!")
    else:
        print(f"At least one of your answers is wrong :( try again!")


def create_check_answer_multi(correct):
    def check_fn(ans):
        check_answers_with_num_multi(ans, correct)
    return check_fn


check_answer_1a = create_check_answer('Toronto', '1a')
check_answer_1b = create_check_answer('Ankara', '1b')
check_answer_1c = create_check_answer('error', '1c')
check_answer_1d = create_check_answer('error', '1d')
check_answer_1e = create_check_answer('error', '1d')
check_answer_1_3 = create_check_answer_multi([4,True,False,False,'error',True,False])


