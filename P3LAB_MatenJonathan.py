 # Jonathan Maten
 # 17 October 2024
 # P3LAB
 # This program converts a money amount into correct change

print('Enter the amount of money as a float: $', end = '')
amount = float(input())
amount = int(amount * 100)

if amount == 0:
    print('No change')

else:
    if amount > 100:
        dollars = amount // 100
        amount = amount - (dollars * 100)
        if (dollars ==1):
            print(dollar, 'Dollar')
        else:
            print(dollars, 'Dollars')

    if amount > 25:
        quarters = amount // 25
        amount = amount - (quarters * 25)
        if quarters ==1:
            print(quarters, 'Quarter')
        else:
            print(quarters , 'Quarters')

    if amount > 10:
        dimes = amount // 10
        amount = amount - (dimes * 10)
        if dimes == 1:
            print(dimes, 'Dime')
        else:
            print(dimes, 'Dimes')

    if amount > 5:
        nickels = amount // 5
        amount = amount - (nickels * 5)
        if nickels == 1:
            print(nickels, 'Nickel')
        else:
            print(nickels, 'Nickels')

    if amount == 1:
        print(amount, 'Penny')
    if 2 <= amount <= 4:
        print(amount, 'Pennies')
    

