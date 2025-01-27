import random

RULE_CALC = "What is the result of the expression?"

def generate_calc_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])
    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)  # Используем eval для вычисления результата
    return question, correct_answer
