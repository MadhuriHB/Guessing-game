# Put your code here
import random

too_low = 0
too_high = 101
guess = None

name = raw_input('Hi! What\'s your name? > ')
print "Hi %s! I am thinking of a number between 1 and 100. " %name
secret_number = random.randint(1, 101)

while (guess!= secret_number):
    guess = int(raw_input('What is my number? > '))
    if (guess < secret_number):
        print('Too low. Guess again.\n')
    elif (guess > secret_number):
        print ("Too high. Guess again. \n")
    
print ("You got it!")