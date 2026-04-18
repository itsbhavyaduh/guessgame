import random

def get_word(difficulty, file_path):
    with open(file_path, "r") as file:
        words = file.read().splitlines()
    return random.choice(words)