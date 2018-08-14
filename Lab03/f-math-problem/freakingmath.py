from random import *
from eval import cacl

def generate_quiz():
    x = randint(1,10)
    y = randint(1,10)
    op = choice(['+','-','*','/'])
    res = cacl(x, y, op)
    
    err = randint(-1,1)
    display_result = res + err
    # Hint: Return [x, y, op, display_result]
    return [x, y, op, display_result]

def check_answer(x, y, op, display_result, user_choice):
    true_res = cacl(x, y, op)
    if true_res == display_result:
        return user_choice
    else:
        return not user_choice
    pass
