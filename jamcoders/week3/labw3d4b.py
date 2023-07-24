from sympy import Symbol, Function, log, sympify

n = Symbol('n')
O = Function('O')

def make_solution_function(correct_answer):
        def solution_function(answer):
            import math
            n = Symbol('n')
            answer = sympify(answer).replace(O, lambda x: x)
            correct = correct_answer.replace(O, lambda x: x)
            if correct.equals(answer):
                print("Test case passed!")
                return

            results = []
            for exp in range(10, 110, 10):
                val = 10 ** exp
                ratio = (answer.subs(n, val) / correct.subs(n, val))
                results.append(log(ratio).evalf())
            inf, sup = min(results), max(results)
            if math.isclose(inf, sup):
                if math.isclose(inf, 0):
                    print("Test case passed!")
                else:
                    print("---------------- Test case failed. ----------------")
                    print(f"Very close! The answer you provided, {repr(answer)},")
                    print("differs from the correct answer by a constant factor.")
                    print("---------------------------------------------------")
                    print()
            else:
                print("---------------- Test case failed. ----------------")
                if results[-1] < 1:
                    print(f"The answer you provided, {repr(answer)}, grows ")
                    print("more slowly than the correct answer.")
                elif results[-1] > 1:
                    print(f"The answer you provided, {repr(answer)}, grows ")
                    print("more quickly than the correct answer.")
                print("---------------------------------------------------")
                print()
        return solution_function


def check_answers(answer, correct, num):
    if correct == answer:
        print(f"Your answer to Question {num} is correct!")
    else:
        print(f"Your answer to Question {num}: '{answer}' is wrong :( try again!")


check_time_complexity = make_solution_function(O(n))
