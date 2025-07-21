options = {
    "font_size": 18,
    "node_size": 1000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 1,
    "width": 1,
}

# For answer checking without revealing the answer
def check_answers_with_num(answer, correct):
    if correct == answer:
        print(f"Your answer is correct!")
    else:
        print(f"Your answer: '{answer}' is wrong :( try again!")


def create_check_answer(correct):
    def check_fn(ans):
        check_answers_with_num(ans, correct)
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


check_answer_0 = create_check_answer([2, 4, 6, 8], '0')
check_answer_1_1 = create_check_answer([0, 1, 4, 2, 3], '1.1')
check_answer_1_2 = create_check_answer([0], '1.2')
check_answer_1_3_1 = create_check_answer(0, '1.3, current_vertex')
check_answer_1_3_2 = create_check_answer([1, 4], '1.3, queue')
check_answer_1_4_1 = create_check_answer(1, '1.4, current_vertex')
check_answer_1_4_2 = create_check_answer([4, 2, 3], '1.4, queue')
check_answer_1_5_1 = create_check_answer(4, '1.5, current_vertex')
check_answer_1_5_2 = create_check_answer([2, 3, 5], '1.5, queue')
check_answer_1_6_1 = create_check_answer(2, '1.6, current_vertex')
check_answer_1_6_2 = create_check_answer([3, 5, 7], '1.6, queue')
check_answer_1_7_1 = create_check_answer(3, '1.7, current_vertex')
check_answer_1_7_2 = create_check_answer([5, 7], '1.7, queue')
check_answer_1_8_1 = create_check_answer(5, '1.8, current_vertex')
check_answer_1_8_2 = create_check_answer([7, 6], '1.8, queue')
check_answer_1_9_1 = create_check_answer(7, '1.9, current_vertex')
check_answer_1_9_2 = create_check_answer([6], '1.9, queue')
check_answer_1_10_1 = create_check_answer(6, '1.10, current_vertex')
check_answer_1_10_2 = create_check_answer([], '1.10, queue')
check_answer_1_11 = create_check_answer([0, 1, 4, 2, 3, 5, 7, 6], '1.11')