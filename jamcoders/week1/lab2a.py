# For answer checking without revealing the answer
def check_answers(answer, correct, num):
    if correct == answer:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")


def check_answer_0_1(answer):
    check_answers(answer, False, "0.1")

def check_answer_0_2(answer):
    check_answers(answer, False, "0.2")

def check_answer_0_3(answer):
    check_answers(answer, True, "0.3")

def check_answer_0_4(answer):
    check_answers(answer, True, "0.4")

def check_answer_0_5(answer):
    check_answers(answer, True, "0.5")

def check_answer_0_6(answer):
    check_answers(answer, False, "0.6")

def check_answer_0_7(answer):
    check_answers(answer, True, "0.7")

def check_answer_0_8(answer):
    check_answers(answer, True, "0.8")

def check_answer_1_1(answer):
    check_answers(answer, "B", "1.1")

def check_answer_1_2(answer):
    check_answers(answer, "C", "1.2")

def check_answer_2_0(answer):
    check_answers(answer, "It's not too hot.", "2.0")

def check_answer_2_4(answer1, answer2):
    answers = [answer1] + [answer2]
    check_answers(answers, [2,1], "2.4")

def check_answer_2_6(answer):
    check_answers(answer, ['Perfect day for the beach!', 'Wear a hoodie and bring a raincoat.', 'Dress warmly, it’s cold out.', 'Wear shorts and take an umbrella.'], "2.6")

def check_answer_3_1(answer_A, answer_B, answer_C, answer_D):
    answers = [answer_A] + [answer_B] +[answer_C] +[answer_D] 
    check_answers(answers, [2,1,4,3], "3.1")

def check_answer_3_4(answer):
    check_answers(answer, "I am cool.", "3.4")
