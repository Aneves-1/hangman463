import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        word_list = ["banana", "apple", "strawberry", "pear", "orange"]
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ["_"]
        self.num_lives = num_lives
        self.num_letter = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
    def check_guess(self, guess):
        guess = lower(self.guess)
        if guess in self.word:
            print("Good guess! {guess} is in the word.")
    def ask_for_input():
    
        while True:
            global guess
            guess = input('Enter your letter choice: ')            
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            elif len(guess) == 1 and guess.isalpha() and guess not in list_of_guesses:
                check_guess()
                list_of_guesses.append(guess)
    ask_for_input()
    