from brain_games.engine import play_game
from brain_games.games.calc import RULE_CALC, generate_calc_question

def main():
    play_game(RULE_CALC, generate_calc_question)

if __name__ == "__main__":
    main()
