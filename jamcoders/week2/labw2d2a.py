def check_answers(answer, correct, num):
    if correct == answer:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")

def check_answer_complement1(answer):
    check_answers(answer, 'TAGGCCCTAGTT', "5.1.1")

def check_answer_complement2(answer):
    check_answers(answer, 'CCGGGGTAAAAG', "5.1.2")