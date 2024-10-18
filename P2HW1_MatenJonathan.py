 # Jonathan Maten

 # 12 October 2024

 # P2HW1

 # A brief description of the project

print('This program calculates and displays travel expenses')
print('') 
print("Enter a budget:", end=" ")
budget = int(input())
print("")

print("Enter a travel destination:", end=" ")
destination = input()
print("")

print("How much do you think you will spend on gas?", end = " ")
gas = int(input())
print("")

print("Approximately, how much will you need for accomodation/hotel?", end=" ")
accomodation = int(input())
print("")

print("Last, how much do you need for food? ", end="")
food = int(input())
print("")

expenses = gas + accomodation + food
total = budget - expenses

print("------------Travel Expenses------------")
print(f'{'Location:':<20} {destination}')
print(f'{'Initial Budget:':<19}  ${budget:.2f}')
print(f'{'Fuel:':<20} ${gas:.2f}')
print(f'{'Accomodation:':<20} ${accomodation:.2f}')
print(f'{'Food:':<20} ${food:.2f}')
print("---------------------------------------")
print("")
print(f'{'Remaining Balance:':<20} ${total:.2f}')

