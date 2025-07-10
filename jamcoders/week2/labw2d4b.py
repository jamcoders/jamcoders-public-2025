def check_answers(answer, correct, num):
    if correct == answer:
        print(f"\033[92mYour answer to Question {num} is correct!\033[0m")
    else:
        print(f"\033[1;95mYour answer to Question {num}: '{answer}' is wrong :( try again!\033[0m  ")

def check_first_basecase(answer):
    check_answers(answer, False, "2.1")

def check_second_basecase(answer):
    check_answers(answer, True, "2.2")
