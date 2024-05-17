from tkinter import *
import random

num = random.randint(0,100) # random.randint function will generate a random number 

# The Guesser Function will take the user input to make guesses
def guesser(count):
    count=count+1
    if(count>10):            #if condition will keep a count of the number of attempts made 
        print("\n\t|------- YOU LOSE -------|")
        print("Maximum Attempts reached ")
        quit()
    guess = int(input("Enter your Guess : "))
    predictor(guess,count)

# The predictor function will check if the guess matches the random number 
def predictor(guess,count):
    if(guess==num):
        print("\n\t|-------- YOU WON ---------| ")
        print("The number is ", guess)
        print("You took", count,"attempts\n")
    elif(guess < num):
         print("Try Again with bigger number than ", guess)
         guesser(count)
   
    elif(guess > num):
        print("Try again with smaller number than ", guess)
        guesser(count)

print("\n\t GUESS THE NUMBER ?????")     
count=0   
guesser(count)        
    
        
    

        