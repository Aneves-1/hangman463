import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        word_list = ["banana", "pear", "strawberry", "apple", "apricot"]
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ["_"]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        list_of_guesses = []
    def check_guess(self, guess):
        guess = str.lower(guess)
        word_lower = str.lower(self.word)
        guess_count = word_lower.count(guess)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            if guess_count >= 1:   
                guess_indices = []
                guess_index = word_lower.index(guess)
                guess_indices.append(guess_index)
                count = 1
                while count < guess_count:
                    guess_index = word_lower.index(guess, guess_indices[-1]+1)
                    guess_indices.append(guess_index)
                    count += 1
                for i in guess_indices:
                    self.word_guessed[i] = guess
            self.num_letters -= 1 
        else:
            self.num_lives -= 1
            print("Sorry, {letter} is not in the word.")
            print("You have {num_lives} lives left.")       
    def ask_for_input(self):
    
        while True:
            global guess
            guess = input('Enter your letter guess: ')            
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            elif len(guess) == 1 and guess.isalpha() and guess not in list_of_guesses:
                check_guess()
                list_of_guesses.append(guess)
        

    