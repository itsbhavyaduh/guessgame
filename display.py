def print_welcome():
    print("Welcome to the Word Guessing Game!")

def choose_difficulty():
    return input("Choose difficulty (easy/medium/hard): ")

def render_game(state):
    display = ""
    for letter in state.word:
        if letter in state.guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)
    print("Attempts left:", state.attempts)

def get_guess(state):
    return input("Enter a letter (or ? for hint): ")

def show_guess_result(result, guess):
    if result == "correct":
        print("Correct!")
    elif result == "wrong":
        print("Wrong!")
    else:
        print("Already guessed!")

def show_hint_result(revealed, difficulty):
    print("Hint revealed:", revealed)

def show_win(state, score):
    print("You won! Score:", score)

def show_loss(state):
    print("You lost! Word was:", state.word)

def ask_play_again():
    return input("Play again? (y/n): ").lower() == "y"

def show_final_score(total_score, games_played, games_won):
    print("\nGames played:", games_played)
    print("Games won:", games_won)
    print("Total score:", total_score)
    