import random

class word_randomization:
    
    word_list=["banana", "apple", "strawberry", "pear", "orange"]
    global word
    word = random.choice(word_list)
    print(word)
word_randomization()

def ask_for_input():
    
    while True:
        global guess
        guess = input('Enter your letter choice: ')
            
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    global lower_convert 
    lower_convert = guess.lower()
    check_guess()

def check_guess():
    guess = lower_convert
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
    
ask_for_input()
