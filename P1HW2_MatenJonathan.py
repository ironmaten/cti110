 # Jonathan Maten
 # 28 September
 # P1HW2
 # This program will help create a budget

#Enter a budget
#Enter a travel destination
#Enter an amount for gas
#Enter an amount for accomodations
#Enter an amount for food

#Add gas, accomodations, and food to create "expenses"
#Subtract expenses from the budget to create "total", which will be the amount remaining

#Display a Travel Expenses Banner
#Display the budget
#Display the destination
#Display the amount spent on fuel
#Display the amount spent on accomodations
#Display the amount spent on food

#Display the total amount remaining after all expenses have been subtracted from the budget

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

print("Last, how much do you need for food?", end="")
food = int(input())
print("")

expenses = gas + accomodation + food
total = budget - expenses

print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("")
print("Fuel:", gas)
print("Accomodation:", accomodation)
print("Food:", food)
print("")
print("Remaining Balance:", total)
