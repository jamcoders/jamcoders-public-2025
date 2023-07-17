def check_answers(answer, correct, num):
    if correct == answer:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")

def check_0_3a(answer):
    check_answers(answer, 88, "0.3a")

def check_0_3b(answer):
    check_answers(answer, 44, "0.3b")

def check_0_4a(answer):
    check_answers(answer, 88, "0.4a")

def check_0_4b(answer):
    check_answers(answer, 44, "0.4b")

def check_1_1a(answer):
    check_answers(answer, 1, "1.1a")

def check_1_1b(answer):
    check_answers(answer, 0, "1.1b")

def check_1_1c(answer):
    check_answers(answer, 2, "1.1c")

def check_1_1d(answer):
    check_answers(answer, 3, "1.1d")

def check_1_1e(answer):
    check_answers(answer, 3, "1.1e")
    
def check_1_1f(answer):
    check_answers(answer, 6, "1.1f")

def check_1_2a(answer):
    check_answers(answer, 1, "1.2a")

def check_1_2b(answer):
    check_answers(answer, 0, "1.2b")

def check_1_2c(answer):
    check_answers(answer, 2, "1.2c")

def check_1_2d(answer):
    check_answers(answer, 3, "1.2d")

def check_1_2e(answer):
    check_answers(answer, 3, "1.2e")
    
def check_1_2f(answer):
    check_answers(answer, 6, "1.2f")

def check_1_2g(answer):
    check_answers(answer, 1, "1.2g")

def check_1_2h(answer):
    check_answers(answer, 0, "1.2h")

def check_1_2i(answer):
    check_answers(answer, 0, "1.2i")

def check_1_2j(answer):
    check_answers(answer, 2, "1.2j")

def check_1_2k(answer):
    check_answers(answer, 2, "1.2k")

def check_1_2l(answer):
    check_answers(answer, 1, "1.2l")

def check_1_2m(answer):
    check_answers(answer, 1, "1.2m")

def check_1_2n(answer):
    check_answers(answer, 2, "1.2n")

def check_1_2o(answer):
    check_answers(answer, 2, "1.2o")

def check_2_1(*answer):
    check_answers(answer, ([1, 100], [51, 100], [51, 74], [51, 61]), "2.1")

def check_2_2(*answer):
    check_answers(answer, ([1, 100], [1, 49], [1, 24], [1, 11], [1, 5], [1, 2]), "2.2")

def check_o_1a(answer):
    check_answers(answer, 1, "O.1a")

def check_o_1b(answer):
    check_answers(answer, 0, "O.1b")

def check_o_1c(answer):
    check_answers(answer, 2, "O.1c")

def check_o_1d(answer):
    check_answers(answer, 3, "O.1d")

def check_o_1e(answer):
    check_answers(answer, 3, "O.1e")

def check_o_1f(answer):
    check_answers(answer, 6, "O.1f")

import numpy as np
from numpy.random import default_rng
from time import sleep
import base64

MAGIC_NUM = 71723
MAGIC_STR = base64.b64decode('SGFwcHkgQmlydGhkYXkgV2lsbGlhbSE=').decode('utf-8')
rng = default_rng()
orders = np.unique(rng.choice(100000, size=10000, replace=False))
if MAGIC_NUM not in orders:
    orders = np.append(orders, MAGIC_NUM)
orders = np.sort(np.unique(orders))
magic_index = np.where(orders == MAGIC_NUM)[0][0]

def get_number_of_orders():
    return len(orders)

def get_order(i):
    sleep(0.5)
    return orders[i]

def get_message(i):
    if i == magic_index:
        return MAGIC_STR
    else:
        return "Sorry, try again!"