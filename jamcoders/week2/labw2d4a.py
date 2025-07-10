def check_answers(answer, correct, num):
    if correct == answer:
        print(f"\033[92mYour answer to Question {num} is correct!\033[0m")
    else:
        print(f"\033[1;95mYour answer to Question {num}: '{answer}' is wrong :( try again!\033[0m  ")

def warmup_check1(answer, bruno_counter):
    check_answers(answer, 14, "WWPD #1")
    if bruno_counter == 0 and answer == 14:
        print("Congrats! You got it on your first try. Call Bruno over to congratulate you :)")

def warmup_check2(answer):
    check_answers(answer, 0, "WWPD #2")

def warmup_check3(answer):
    check_answers(answer, [3, 2, 1, 0, 1, 2, 3], "WWPD #3")
