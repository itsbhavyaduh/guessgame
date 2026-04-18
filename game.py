class GameState:
    def __init__(self, word, difficulty):
        self.word = word
        self.guessed = []
        self.attempts = 6
        self.is_over = False
        self.is_won = False

    def guess(self, letter):
        if letter in self.guessed:
            return "repeat"

        self.guessed.append(letter)

        if letter not in self.word:
            self.attempts -= 1

        if all(l in self.guessed for l in self.word):
            self.is_over = True
            self.is_won = True

        if self.attempts <= 0:
            self.is_over = True

        return "correct" if letter in self.word else "wrong"

    def use_hint(self):
        for letter in self.word:
            if letter not in self.guessed:
                self.guessed.append(letter)
                return letter
        return None

    def calculate_score(self):
        return self.attempts * 10

def create_game(word, difficulty):
    return GameState(word, difficulty)