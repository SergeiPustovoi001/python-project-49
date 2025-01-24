from brain_games.engine import play_game
from brain_games.games.even import RULE_EVEN, generate_even_question

def main():
    play_game(RULE_EVEN, generate_even_question)

if __name__ == "__main__":
    main()
