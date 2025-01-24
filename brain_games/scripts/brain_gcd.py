from brain_games.engine import play_game
from brain_games.games.gcd import RULE, generate_question

def main():
    """Запускает игру."""
    play_game(RULE, generate_question)
