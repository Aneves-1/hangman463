import random
word_list=["banana", "apple", "strawberry", "pear", "orange"]

def random_choice():
    global word
    word = random.choice(word_list)
random_choice()      
print(word)

choice = input('Enter your letter choice: ')

def letter_choice():
    if len(choice) == 1 and choice.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
letter_choice()