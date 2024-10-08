# -*- coding: utf-8 -*-
"""PythonClass.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11XxepBJxaS1xJvBKv9aWsdiJlQrm3IZv
"""

class Bird:
    def printSize(self):
        print('small')

class Eagle(Bird):
    def printSize(self):
        print('large')

bird = Bird() # Creating an instance of the Bird class
bird.printSize() # Calling the printSize method of the Eagle class

eagle = Eagle()  # Creating an instance of the Bird class
eagle.printSize()  # Calling the printSize method of the Eagle class

'''To create a for loop you need the following:
   for keyword
   a variable -- whose value will change on each loop iteration. In the case above it is called number
   the in keyword
   the range() function - which is an built-in function in the Python library to create a sequence of numbers
   range() takes up to three keyword arguments: set the start (inclusive, default = 0), end (exclusive) and step (default = 1)
range(start, stop, step)'''

for num in range(10):
    print(num)

def square_list_items(to_square):
    """
    Returns a list of numeric value that are
    the square on an input list

    Keyword arguments:
    to_square -- the list of numeric values to square
    """
    result_list = []

    for item in to_square:
        result_list.append(item**2)

    return result_list

my_list = [1, 2, 3, 4, 5]
result = square_list_items(my_list)
print(result)

lista = [2, 3, 5, 7, 8, 10]

listb = []

for num in lista:
    listb.append(num**2)

print(listb)

def square():

    listc = []

    for i in lista:
        listc.append(i**2)

    return listc

listc = square()
listb

def square_list_items(to_square):

    listd = []

    for num in to_square:
        listd.append(num**2)

    return listd

listd = square_list_items(lista)

listd

my_numba = [1, 2, 4, 6, 22, 25, 30]

my_numbb = square_list_items(my_numba)

my_numbb

numb = square_list_items([40, 200, 1000])

numb

def square_list_items(to_square):
    """
    Returns a list of numeric value that are
    the square on an input list

    Keyword arguments:
    to_square -- the list of numeric values to square
    """
    result_list = []

    for index in range(len(to_square)):
        result_list.append(to_square[index]**2)

    return result_list

my_list = [1, 2, 3, 4, 5]
result = square_list_items(my_list)
print(result)

def square_list_item(to_square):

    liste = []

    for index in range(len(to_square)):
        liste.append(to_square[index]**2)

    return liste

my_list = [1, 2, 3, 4, 5]

liste = square_list_item(my_list)

liste

def guessed_correctly(guess, correct_answer):
    '''
    Returns True or False to indicate if user has guessed correctly.

    Keyword arguments:
    guess -- user's guess
    correct_answer -- the answer that needs to be guessed!
    '''
    return guess == correct_answer


def play_game(correct_answer):
    '''
    A game to guess a integer number (between 1 and 10).
    Re-prompts user for guess until correct one is supplied.

    Keyword arguments:
    correct_answer -- specified by user
    '''

    guess = -1

    while not guessed_correctly(guess, correct_answer):
        guess = int(input("Please guess a whole number between 1 and 10: >>"))

    print("Well done you guessed correctly!")


#a test: this returns false because the user guessed incorrectly
result = guessed_correctly(guess=5, correct_answer=10)
print(result)

#a test: this returns true because the user guessed correctly
result2 = guessed_correctly(guess=10, correct_answer=10)
print(result2)

#rather than repeatedly calling guessed_correctly we have created a loop.
#while guessed_correctly returns false
#we continue to re-prompt the user for another guess.
play_game(10)

def guessed_correctly(guess, correct_answer):

    return guess == correct_answer

def play_game(guess):

    guess = -2

    while not guessed_correctly(guess, correct_answer = 15):
        guess = int(input("Please guess a whole number between 5 and 20: >>"))

    print("Well done you guessed correctly!")

    return

play_game(15)

guessed_correctly(guess = 6, correct_answer = 6)

def play_game(correct_answer, lives=3):
    '''
    A game to guess a integer number (between 1 and 10).
    Re-prompts user for guess until correct one is supplied.

    Keyword arguments:
    correct_answer -- specified by user
    lives -- the number of guesses a user is allowed to
    make before they lose the game (default = 3)
    '''

    guess = -1

    while lives > 0:

        guess = int(input("Please guess a whole number between 1 and 10: >>"))

        if guessed_correctly(guess, correct_answer):
            print("Well done you guessed correctly!")
            break # you win! no need to continue! break the loop

        else:
            lives -= 1

    else:
        #code executed becasue lives > 0 = False
        print('Sorry no lives left - you lose!')


play_game(10)