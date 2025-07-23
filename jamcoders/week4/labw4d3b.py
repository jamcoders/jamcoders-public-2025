def check_answers_with_num(answer, correct, num):
    if correct == answer:
        print(f"\033[92mYour answer to Question {num} is correct!\033[0m")
        #print("\033[92mTest case passed.\033[0m")
    else:
        print(f"--------- \033[1;95mYour answer to Question {num}: '{answer}' is wrong :( try again!\033[0m ---------")


        # print("\033[92mTest case passed.\033[0m")
        # print("--------- \033[1;95mTest case failed.\033[0m ---------")


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


check_answer_1 = create_check_answer("Heyela", "1")
check_answer_2a = create_check_answer([1, 3, "westminister"], "2: second")
check_answer_2b = create_check_answer("mini-me", "2: third")
check_answer_3a = create_check_answer(40, "3: a")
check_answer_3b = create_check_answer("error", "3: b")
check_answer_3c = create_check_answer(["uwi!", 2025], "3: c")
check_answer_4a = create_check_answer([30, 2, 4, 32, 40, 5], "4: d")
check_answer_4b = create_check_answer([1, 2, 3, 8, 10, 12, 14], "4: e")
check_answer_5 = create_check_answer([12, 5, 1], "5")
check_answer_6 = create_check_answer([5, 2, 0, 4, 0, 10, 1, 0, 2, 0], "6")
check_answer_7a = create_check_answer([1, 2, 3, 6, 15, 10], "7a")
check_answer_7b = create_check_answer([1, 3, 4, 7, 6, 5, 9], "7b")
check_answer_7c = create_check_answer([1, 2, 3, 4, 5, 7, 8, 6, 9, 10], "7c")
check_answer_8_orange = create_check_answer([9, 32], "8: orange")
check_answer_8_green = create_check_answer([7, 17], "8: green")
check_answer_8_red = create_check_answer([21, 30], "8: red")
check_answer_8_blue = create_check_answer([8, 19], "8: blue")
check_answer_8_purple = create_check_answer([7, 9, 17, 32], "8: purple")
check_answer_8_yellow = create_check_answer([8, 19, 21, 30], "8: yellow")
check_answer_9a = create_check_answer([
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
], "9a")
check_answer_9b = create_check_answer([
    [1, 5],
    [0, 6],
    [3],
    [2, 4],
    [3, 6],
    [0, 7],
    [1, 4, 7],
    [5, 6]
], "9b")
check_answer_9c = create_check_answer(False, "9c")
check_answer_9d = create_check_answer(True, "9d")
check_answer_9e = create_check_answer([0, 1, 6, 4, 3, 2, 7, 5], "9e")
check_answer_9f = create_check_answer([0, 1, 5, 6, 7, 4, 3, 2], "9f")
check_answer_10a = create_check_answer([
  [0, 1, 1, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 0, 0, 0, 1, 0, 0]
], "10a")
check_answer_10b = create_check_answer([
  [1, 2, 3],
  [6],
  [1, 3, 4],
  [5],
  [1, 6],
  [2, 4, 7],
  [],
  [4, 6, 8],
  [6]
], "10b")
check_answer_10c = create_check_answer(False, "10c")
check_answer_10d = create_check_answer(True, "10d")
check_answer_10e = create_check_answer([0, 1, 6, 2, 3, 5, 4, 7, 8], "10e")
check_answer_10f = create_check_answer([0, 1, 2, 3, 6, 4, 5, 7, 8], "10f")
check_answer_16 = create_check_answer(3, "16")
check_answer_17 = create_check_answer(2, "17")
check_answer_18 = create_check_answer(3, "18")
check_answer_19 = create_check_answer(4, "19")
check_answer_20 = create_check_answer(3, "20")
check_answer_21 = create_check_answer(3, "21")