def check_answers(answer, correct, num):
    if correct == answer:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")

def check_first_basecase(answer):
    check_answers(answer, False, "2.1")

def check_second_basecase(answer):
    check_answers(answer, True, "2.2")
