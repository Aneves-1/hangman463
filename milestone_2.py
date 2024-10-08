import random
class word_randomization:
    
    word_list=["banana", "apple", "strawberry", "pear", "orange"]
    global word
    word = random.choice(word_list)
    print(word)
word_randomization()

guess = input('Enter your letter choice: ')

def guess_input_check():
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
guess_input_check()