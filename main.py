import os
import sys

from word_loader import get_word
from game import create_game
from display import (
    print_welcome,
    choose_difficulty,
    render_game,
    get_guess,
    show_guess_result,
    show_hint_result,
    show_win,
    show_loss,
    ask_play_again,
    show_final_score,
)

WORDS_FILE = os.path.join(os.path.dirname(__file__), "data", "words.txt")

def play_round(difficulty):
    word = get_word(difficulty, WORDS_FILE)
    state = create_game(word, difficulty)

    while not state.is_over:
        render_game(state)
        raw = get_guess(state)

        if raw == "?":
            revealed = state.use_hint()
            show_hint_result(revealed, difficulty)
        else:
            result = state.guess(raw)
            show_guess_result(result, raw)

    score = state.calculate_score()

    if state.is_won:
        show_win(state, score)
    else:
        show_loss(state)

    return state.is_won, score

def main():
    print_welcome()

    total_score = 0
    games_played = 0
    games_won = 0

    while True:
        difficulty = choose_difficulty()
        won, score = play_round(difficulty)

        games_played += 1
        if won:
            games_won += 1
            total_score += score

        if not ask_play_again():
            break

    show_final_score(total_score, games_played, games_won)

if __name__ == "__main__":
    main()