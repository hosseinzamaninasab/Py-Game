import random

print('Welcome To My Guess Game')
print('It\'s created on Friday morning, 3 p.m, 25 September, 2020')
print('-----------------------------------------------------------')
print('You\'ll consider a number between 1 to 100 and I will guess it')
print('If i guessed smaller number tell me with \'s\', if i guessed larger number tell me with \'l\' and if it was '
      'right, just hit the enter')
print('OK! Let Us Begin')
print('*******************')

computer_guess = random.randint(1, 100)
print(computer_guess)
a = 1  # for the first time we need the a = 1 ...
b = 100  # also b = 100
counter = 0
limit = 0
while True:
    counter += 1
    limit += 1
    your_response = input('s or l:\n')
    if your_response == 's':
        a = computer_guess
        computer_guess = random.randint(a, b)  # first one, b = 100
        print('computer guess at', counter, ' times is', computer_guess)
    elif your_response == 'l':
        b = computer_guess
        computer_guess = random.randint(a, b)  # first one, a = 1
        print('computer guess at', counter, 'times is', computer_guess)
        if limit == 10:  # set a limit range for computer
            print("oooh You lose dumy!")
            break
    else:
        print('Wow! You make it, smart boy *___* ')
        break
