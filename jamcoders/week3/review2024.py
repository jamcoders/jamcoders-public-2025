def create_solution_functions():
    import sympy
    from sympy import Symbol, Function, log, sympify

    n = Symbol('n')
    O = Function('O')

    solutions = {
        "1_1" : 80,
        "1_2" : 0.8,
        "1_3" : 2,
        "1_4" : 1,
        "1_5" : 3,
        "2_1" : int,
        "2_2" : str,
        "2_3" : str,
        "2_4" : str,
        "2_5" : float,
        "2_6" : int,
        "2_7" : bool,
        "2_8" : list,
        "2_9" : bool,
        "2_10" : dict,
        "2_11" : int,
        "3_1_1" : True,
        "3_1_2" : False,
        "3_2" : ["hello", "there", "what", "whom"],
        "4_1" : ["Needs Improvement", "Excellent", "Good"],
        "4_2" : ["hello", "hello", "hello"],
        "5_3" : [12, 6, 22, 12, 6, 22, 12, 6, 22, 44, 'a', 'b'],
        "9_1" : "Constant",
        "9_2" : "Quadratic"

    }


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

    # globals_ = globals()
    for question, solution in solutions.items():
        name = f"check_answer{question}"
        fn = make_solution_function(solution)
        fn.__name__ = name
        globals()[name] = fn


create_solution_functions()