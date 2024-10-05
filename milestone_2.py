import random
word_list=["banana", "apple", "strawberry", "pear", "orange"]

def choose_random_word():
    global word
    word = random.choice(word_list)
choose_random_word()      
print(word)

guess = input('Enter your letter choice: ')

def guess_input_check():
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
guess_input_check()