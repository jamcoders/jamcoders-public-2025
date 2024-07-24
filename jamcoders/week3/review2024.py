def create_solution_functions():

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
            if correct_answer == answer:
                print("Test case passed!")
            else:
                print(f"Your answer is wrong :( try again!")

        return solution_function

    # globals_ = globals()
    for question, solution in solutions.items():
        name = f"check_answer{question}"
        fn = make_solution_function(solution)
        fn.__name__ = name
        globals()[name] = fn


create_solution_functions()