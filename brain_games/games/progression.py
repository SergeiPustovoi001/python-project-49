import random

RULE = "What number is missing in the progression?"

def generate_question():
    """Генерирует арифметическую прогрессию с пропущенным числом."""
    length = random.randint(5, 10)  # длина прогрессии от 5 до 10
    start = random.randint(1, 20)   # первое число прогрессии
    step = random.randint(2, 5)     # шаг прогрессии от 2 до 5

    progression = [start + i * step for i in range(length)]
    
    # Скрываем случайное число из прогрессии
    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'

    # Возвращаем строку прогрессии и правильный ответ
    question = " ".join(map(str, progression))
    return question, str(hidden_value)
