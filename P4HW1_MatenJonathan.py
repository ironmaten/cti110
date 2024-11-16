# Jonathan Maten
# 10 November 2024
# P4HW1
# This program makes a list of scores, determines the lowest value and removes it, then creates an average from the remaining values and gives a letter grade

#Create a list for all the scores under score_list
#Obtain the total number of scores recorded as number_of_scores
#Create a for loop to enter in all score values
#Created a nested while loop that checks if the score is between 0 and 100 and requires the user to input another value if it is outside the range
#Convert the scores to float values, then add to score_list
#Determine the lowest score using a for loop and recordit as lowest_score
#Remove the lowest score from score_list
#Determine the average of all the scores and record as average_score
#Create if branches that check what the average score is and assigns a corresponding letter grade
#Create a print screen showing Results, Lowest Score, Modified List, Scores Average, and Grade

score_list = []
number_of_scores = int(input(f'How many scores do you want to enter? ')) +1
print('')

for i in range(1, number_of_scores):
    score = int(input(f'Enter score #{i}: '))
 
    while score <0 or score >100:
        print('')
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        score = int(input(f'Enter score #{i} again: '))
    score = float(score)
    score_list.append(score)
    
lowest_score = score_list[0]
for i in range(0, number_of_scores -1):
    if score_list[i] < lowest_score:
        lowest_score = score_list[i]
score_list.remove(lowest_score)
average_score = sum(score_list) / (number_of_scores - 2)

if average_score <60:
     grade = 'F'
if average_score >=60:
    grade = 'D'
if average_score >70:
    grade = 'C'
if average_score >80:
    grade = 'B'
if average_score >90:
    grade = 'A'
    
print('')
print('')
print('--------------Results-----------')
print(f'Lowest Score : {lowest_score}')
print(f'Modified List : {score_list}')
print(f'Scores Average: {average_score:.2f}')
print(f'Grade: {grade}')
print('--------------------------------')
