import random

def generate_question():
    """Генерирует случайное число и возвращает его."""
    return random.randint(1, 100)

def is_even(number):
    """Проверяет, чётное ли число."""
    return number % 2 == 0

def play_game():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    
    correct_answers = 0
    while correct_answers < 3:
        number = generate_question()
        print(f"Question: {number}")
        
        user_answer = input("Your answer: ").lower()
        correct_answer = "yes" if is_even(number) else "no"
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again!")
            return

    print("Congratulations, you won!")

def main():
    play_game()

if __name__ == "__main__":
    main()