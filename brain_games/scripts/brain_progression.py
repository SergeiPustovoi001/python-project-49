from brain_games.engine import play_game
from brain_games.games.progression import RULE, generate_question

def main():
    """Запускает игру арифметической прогрессии."""
    play_game(RULE, generate_question)

