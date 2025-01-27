from brain_games.engine import play_game
from brain_games.games.prime import RULE, generate_question

def main():
    """Запускает игру Простое ли число."""
    play_game(RULE, generate_question)
