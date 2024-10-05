import random
word_list=["banana", "apple", "strawberry", "pear", "orange"]

def random_choice():
    global word
    word = random.choice(word_list)
random_choice()      
print(word)

guess = input('Enter your letter choice: ')

def letter_choice():
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
letter_choice()