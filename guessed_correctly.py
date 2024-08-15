# -*- coding: utf-8 -*-
"""guessed_correctly.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gB-wkeGLKZkjfuSNfAMwzXCVNlHEMUsJ
"""

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