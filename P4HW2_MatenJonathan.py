 # Jonathan Maten
 # 10 November 2024
 # P4HW2
 # This program takes information regarding employees and calculates pay. It then gives total statistics

#Get employee name, number of hours worked, and their pay rate
#Initialize overtime pay, hours, total overtime, total regular hours, and total gross to 0

num_employees = 0
total_overtime = 0.0
total_regular = 0.0
total_gross = 0.0

name = input('Enter employee\'s name: ')
while name != 'Done':
    total_hours = float(input('Enter number of hours worked: '))
    pay_rate= float(input('Enter employee\'s pay rate: '))
    overtime_pay = 0.0
    overtime_hours = 0.0

#Create an if/else loop that checksif total hours are over 40.

#If >40, calculate the number of overtime hours (overtime_hours), the amount paid
#for overtime (overtime_pay), and the amout paid at the normal pay rate for the first 40 hours(reg_hour_pay)

#Else calculate the amount of hours worked multiplied by the pay rate and assign to reg_hour_pay
    if total_hours > 40:
        overtime_hours = total_hours - 40
        overtime_pay = overtime_hours * 1.5 * pay_rate
        reg_hour_pay = 40 * pay_rate
    else:
        reg_hour_pay = total_hours * pay_rate

#calculate gross pay with overtime + reg_hour_pay
    gross_pay = overtime_pay + reg_hour_pay

#Add the employee to the total number, then add the employee's pay to the total paid for overtime, total paid for regular hours, and total gross paid

    num_employees += 1
    total_overtime = total_overtime + overtime_pay
    total_regular = total_regular + reg_hour_pay
    total_gross = total_gross + gross_pay
    
#output a table with Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay, and Gross_pay with set widths

    print('')
    print('Employee name:    ', name)
    print('')
    print(f'{'Hours Worked':<15} {'Pay Rate':<12} {'OverTime':<12} {'OverTime Pay':<20} {'RegHour Pay':<20} {'GrossPay':<20}')
    print('----------------------------------------------------------------------------------------------------------------------')
    print(f'{total_hours:<15} {pay_rate:<12.2f} {overtime_hours:<12} {overtime_pay:<20} ${reg_hour_pay:<19.2f} ${gross_pay:<19.2f}')

    name = input('Enter employee\'s name or \"Done\" to terminate: ')

#Display the total numbers of employees, total overtime pay, total regular pay, and total gross pay
print('')
print(f'Total number of employees entered: {num_employees}')
print(f'Total amount paid for overtime: ${total_overtime}')
print(f'Total amount paid for regular hours: ${total_regular}')
print(f'Total amount paid in gross: ${total_gross}')
