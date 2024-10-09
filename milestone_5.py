import random

class Hangman:
    '''
    A Hangman Game that asks the user to guess a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the guessed letter is in the word.
    ask_for input()
        Asks the user to guess a letter.
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ["_"]
        self.num_lives = int(num_lives)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    def check_guess(self, guess):
        '''
        Checks if the guessed letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter that was guessed to be checked

        '''
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
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)
        print(f"{self.word_guessed}")
                 
    def ask_for_input(self):
        '''
        Asks the user for a letter guess and checks two things:
        1. If the character is a single character
        2. If the letter has already been tried
        If it passes both checks, it calls the check_guess method.
        '''
        while True:
            guess = input("Enter your letter guess: ")            
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            elif len(guess) == 1 and guess.isalpha() and guess not in self.list_of_guesses:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
             
def play_game(word_list):
    
    game = Hangman(word_list, num_lives = 5)
    while True:
        
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break    
if __name__ == "__main__":
    word_list = ["banana", "pear", "strawberry", "apple", "apricot"]
    play_game(word_list)

