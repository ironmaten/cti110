# Jonathan Maten
# 1 October 2024
# P2LAB2
# This project involves the creation of a dictionary

my_dict = {
    'Camaro' : 18.21,
    'Prius' : 52.36,
    'Model S' : 110,
    'Silverado' : 26
}

keys = my_dict.keys()

print(keys)

print('Enter a vehicle to see it\'s mpg: ', end = "")
vehicle = input()
print('')

print('The', vehicle,'gets', my_dict[vehicle], 'mpg.')
print('')

print('How many miles will you drive the', vehicle, end="")
print('? ', end = '')
miles = float(input())
print('')

gas_needed = miles / my_dict[vehicle]

print(f'{gas_needed:.2f}', 'gallon(s) of gas are needed to drive the', vehicle, miles, 'miles')