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
        word_lower = str.lower(self.word)
        guess_count = word_lower.count(guess)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.num_letter -= 1
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
            
                print(f'{self.word_guessed}')
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)
        print(f'Letters tried: {set(self.list_of_guesses)}')
        print(self.num_letter)           
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
    
    game = Hangman(word_list, num_lives = 5)
    while True:
        game.ask_for_input()
        if game.num_letter == 0:
            print("Congratulations. You won the game!")
            break
        elif game.num_lives == 0:
            print("You lost!")
            break
       
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)

