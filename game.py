# Put your code here
import random

name = raw_input("Hi! What\'s your name? >>> ")
print "Hi %s! I am thinking of a number between 1 and 100. " %name
secret_number = random.randint(1, 101)

guess = None
while (guess != secret_number):
    try:
        guess = int(raw_input("What is my number? >>> "))
    except ValueError:
        print "That was not a valid number!\n" 
        continue


    if(guess<1 or guess>100):
        print "That number is out of bounds.\n"
    else:    
        if(guess < secret_number):
            print("Too low. Guess again.\n")
        elif (guess > secret_number):
            print ("Too high. Guess again. \n")
    
print ("You got it!")