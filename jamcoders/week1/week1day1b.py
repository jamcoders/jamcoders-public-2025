def check_expression1(expression):
    print(f'   A    | Your Answer ')
    print(f'--------|-------------')
    print(f'  True  |  {expression(True)}  ')
    print(f'  False |  {expression(False)}   ')


def check_expression2(expression):
    print(f'   A    |    B    | Your Answer ')
    print(f'--------|---------|--------------')
    print(f'  True  |  True   |  {expression(True, True)}  ')
    print(f'  True  |  False  |  {expression(True, False)}  ')
    print(f'  False |  True   |  {expression(False, True)}  ')
    print(f'  False |  False  |  {expression(False, False)}  ')
