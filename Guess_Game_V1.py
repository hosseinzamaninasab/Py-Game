import random

rand_number = random.randint(1, 100)  # for given us a random number between 1, 100
print("Welcome To My Game")
print('It is created on Thursday morning, 4 a.m, 24 September, 2020')
print('------------------------------------------------------------')
name = input("Hi, what's your name:\n")
counter = 0
guess = 0  # counter for set limit and guess for find out hoe many times took to guess the number
while True: 
    counter += 1
    guess += 1
    number = int(input("Guess my number:\n"))
    if counter == 10:
    	print("you lose!", name)
    	break  # after lose the program must stoped
    if rand_number > number:  # guidance to guess better
    	print(name, "guess a bigger one")
    elif rand_number < number:  # guidance to guess better
    	print("guess a smaller one", name)
    else:
	    print("yay!!! you win ^___^", name, ", after", guess, "guesses")
	    break
