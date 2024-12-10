 # Jonathan Maten
 # 23 November 2024
 # P5HW
 # This is a math quiz program that offers addition and subtraction problems

import random

#defining the adding function
def adding_random_numbers(int1, int2):
    num_of_guesses = 1
    total = int1 + int2
    
    print(f'{int1:>6}')
    print(f'+ {int2:>4}')
    print('')
    print('Enter answer.')

    guess = int(input())
    
    while guess != total:
        if guess > total:
            print('Sorry, guess is too high.')
            print('')
            guess = int(input('Try again: '))
            num_of_guesses += 1
        else:
            print('Sorry, guess is too low.')
            print('')
            guess = int(input('Try again: '))
            num_of_guesses += 1
            
    print('Congratulations!!!! Your answer is correct.')
    print(f'Number of guesses: {num_of_guesses}')
    print('')
    
#defining the subtracting function    

def subtracting_random_numbers(int1, int2):
    num_of_guesses = 1
    total = int1 - int2
    
    print(f'{int1:>6}')
    print(f'- {int2:>4}')
    print('')
    print('Enter answer.')

    guess = int(input())
    
    while guess != total:
        if guess > total:
            print('Sorry, guess is too high.')
            print('')
            guess = int(input('Try again: '))
            num_of_guesses += 1
        else:
            print('Sorry, guess is too low.')
            print('')
            guess = int(input('Try again: '))
            num_of_guesses += 1
            
    print('Congratulations!!!! Your answer is correct.')
    print(f'Number of guesses: {num_of_guesses}')
    print('')

#main program with greeting
print('Welcome to Math Quiz')
print('')
print('')
option = '0'

#main menu 
while option != '3':
    random_num1 = random.randint(1, 1000)
    random_num2 = random.randint(1, 1000)
    

    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print('')
    option = input('Please choose one of the menu options: ')

#calling the functions
    if option == '1':
        adding_random_numbers(random_num1, random_num2)
    elif option == '2':
        subtracting_random_numbers(random_num1, random_num2)
    elif option == '3':
        break
    else:
        print('Invalid option, please select an option that is 1 through 3')
        print('')

print('Thank you for playing...')
print('Bye!!')
