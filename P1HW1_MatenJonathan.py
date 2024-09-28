 # Jonathan Maten
 # 27 September 2024
 # P1HW1
 # This program executes simple mathematical expressions

print('-----Calculating Exponents----')
print("")
print("")

print('Enter an integer as the base value:', end=" ")
base_value = int(input())
print('Enter an integer as the exponent:', end=" ")
exponent = int(input())
print("")
print("")

total1 = base_value ** exponent
print(base_value, 'raised to the power of', exponent, 'is', total1, '!!')
print("")
print("")

print('-----Addition and Subtraction----')
print("")
print("")

print('Enter a starting integer:', end=" ")
starting_int = int(input())

print('Enter an integer to add:', end=' ')
addition_int = int(input())

print('Enter an integer to subtract:', end=" ")
subtraction_int = int(input())
print('')
print('')

total2 = starting_int + addition_int - subtraction_int

print(starting_int, '+', addition_int, '-', subtraction_int, 'is equal to', total2)