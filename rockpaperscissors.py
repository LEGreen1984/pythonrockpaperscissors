#creates an array of options to randomise.
choices = ["rock", "paper" , "scissors"]
#imports the random function
import random

playerchoice = input('rock, paper, scissors?')
computerchoice = random.choice(choices)

#this function matches the player choice against computer's option
def compare(c, u):
    if c == u:
        print("this was a draw ")
    elif c == 'rock' and u == 'scissors':
        print("rock beats scissors, you lose!")
    elif c == 'rock' and u == 'paper':
        print("Paper covers rock, you win!")
    elif c == 'scissors' and u == 'paper':
        print("scissors slice paper, you lose!")
    elif c == 'scissors' and u == 'rock':
        print("rock blunts scissors, victory!")
    elif c == 'paper' and u == 'rock':
        print("paper covers rock, you lose!")
    elif c == 'paper' and u == 'scissors':
        print("paper slices scissors, you win!")

#calls the compare function with your choice and the randomised computer choice as the variables
compare(computerchoice, playerchoice)
