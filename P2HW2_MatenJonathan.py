 # Jonathan Maten

 # 12 October 2024

 # P2HW2

 # This program compiles all the grades for each module and gives various statistics

 #Create a blank list
 #Assign Module 1 grade as the first element at index 0
 #Assign Module 2 grade as the first element at index 1
 #Assign Module 3 grade as the first element at index 2
 #Assign Module 4 grade as the first element at index 3
 #Assign Module 5 grade as the first element at index 4
 #Assign Module 6 grade as the first element at index 5
 #Create a value for average by taking the sum of all elements of the list and dividing by 6
 #Output a Results header
 #Output the lowest grade using the min function
 #Output the highest grade using the max function
 #Output the sum of all grades using the sum function
 #Output the average calculated earlier
 #Output a string of hyphens

grades = [0, 0, 0, 0, 0, 0]
print('Enter grade for Module 1: ', end='')
grades[0] = float(input())
print('Enter grade for Module 2: ', end='')
grades[1] = float(input())
print('Enter grade for Module 3: ', end='')
grades[2] = float(input())
print('Enter grade for Module 4: ', end='')
grades[3] = float(input())
print('Enter grade for Module 5: ', end='')
grades[4] = float(input())
print('Enter grade for Module 6: ', end='')
grades[5] = float(input())

average = sum(grades) / 6

print('')
print('------------Results------------')
print(f'{'Lowest Grade:':<20} {min(grades)}')
print(f'{'Highest Grade:':<20} {max(grades)}')
print(f'{'Sum of Grades:':<20} {sum(grades)}')
print(f'{'Average:':<20} {average:.2f}')
print('----------------------------------------')
