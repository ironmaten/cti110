 # Jonathan Maten
 # 20 October 2024
 # P4LAB2
 # This program involves using loops to create a multiplication table and take multiple inputs using for and while loops.

run_program = 'yes'

while run_program == 'yes':
    integer = int(input('Enter an integer: '))
    print('')
    if integer >= 0:
        for i in range(1, 13):
            print(f'{integer} * {i} = {integer * i}')
        print('')
    else:
        print('This program does not handle negative numbers')
        print('')
    run_program = input(f'Would you like to run the program again? ')
    print('')
    while run_program != 'yes':
        if run_program == 'no':
            break
        else:
            run_program = input(f'Invalid response. Please answer \'yes\' or \'no\': ')
            print('')

print('Exiting program...')
