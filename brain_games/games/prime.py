def is_prime(number):
    """Проверяет, является ли число простым."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def generate_question():
    """Генерирует случайное число и возвращает вопрос и правильный ответ."""
    import random
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), correct_answer

