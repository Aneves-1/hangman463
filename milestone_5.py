import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ["_"]
        self.num_lives = num_lives
        self.num_letter = len(set(self.word))
        self.list_of_guesses = []
    def check_guess(self, guess):
        guess = str.lower(guess)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.list_of_guesses.append(guess)
            for i in range(0, len(self.word)):
                if self.word_guessed[i] == guess:
                    self.word_guessed[i] == guess
                self.num_letter -= 1
                print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")       
    def ask_for_input(self):
    
        while True:
            guess = input('Enter your letter choice: ')            
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            elif len(guess) == 1 and guess.isalpha() and guess not in self.list_of_guesses:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives = 5)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letter > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letter == 0:
            print("Congratulations. You won the game!")
word_list = ["banana", "apple", "strawberry", "pear", "orange"]
play_game(word_list)

