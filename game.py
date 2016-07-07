    # Put your code here
import random

def guessing_game():
    retry = "y"
    best_score = 1000
    while(retry == "y"):
        name = raw_input("What\'s your name? >>> ")
        print "Hi %s! I am thinking of a number between 1 and 100. " %name
        secret_number = random.randint(1, 101)

        guess = None
        score = 0
        while (guess != secret_number):

            try:
                guess = int(raw_input("What is my number? >>> "))
                score = score + 1
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
        print score
        print best_score
        if(score < best_score):
            best_score = score
        print "You got it! Your score was %d.\n Your previous best (lowest) was %d.\n" % (score, best_score)    
        retry = raw_input("Do you want to play again? Press y/n. >>> ")
   
    print "Thank you for playing!\n"
    return

guessing_game()
