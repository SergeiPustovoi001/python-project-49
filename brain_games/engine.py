import prompt

def play_game(rule, generate_question):
    """Запускает игру с указанными правилами и функцией для генерации вопросов."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(rule)

    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        # Приводим правильный ответ и ввод пользователя к строке для корректного сравнения
        if str(user_answer) == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
