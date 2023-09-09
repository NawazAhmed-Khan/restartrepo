
def dwg_sal():
    rate_hour = float(input('\tEnter the working rate  per hour in $ '))
    working_hour = float(input('\tEnter the daily working hour '))
    daily_wage = working_hour * rate_hour
def ful_month_sal():
    monthly_working_days = float(input('\tEnter The Full Month Working days '))
    monthly_basic_salary = monthly_working_days * daily_wage
    print("\tThe Monthly Basic Salary without taxes are $", monthly_basic_salary)
    house_rent = (monthly_basic_salary * 40) / 100
    print('\tThe House Rent is $', house_rent)
    medical_allownce = (monthly_basic_salary * 30) / 100
    print('\tThe Medical Allownces are $', medical_allownce)
    gross_salary = monthly_basic_salary + house_rent + medical_allownce
    print('\tThe Monthly Gross Salary Without Taxes are $', gross_salary)
    taxes = (gross_salary * 25) / 100
    print('\tTax deductions are $', taxes)
    net_salary = gross_salary - taxes


print('\t****************** Daily Wages Pay Slip Calculator ***************   ')
print("\tThe Daily Wage as per rate without taxes are $")
dwg_sal()
print('\t**************Full Month Salary Slip*************')
print('\tThe Full Mont Net Salary after Tax deductions are $')
ful_month_sal()

pin = input('Enter the PINCODE')
pinlength = len(pin)
if pinlength != 4 or pin != pincode:
print('Please Enter the pincode again(4 digits)')
else:
break
while(True):
print('*************** Welcome to ATM Machine ****************')
print('\t\t 1. Withdraw Amount')
print('\t\t 2. Deposit Amount')
print('\t\t 3. Balance Inquiry')
print('\t\t 4. Exit')
choice = input('Enter the option')
if choice == '1':
while(True):
amount = int(input('Enter the amount to withdraw'))
if amount <= balance:
balance = balance - amount
print(f'The Remaining balance is {balance}')
break
else:
print('Entered amount is greater than the available balance')
cont = input('Do you want to do another Transaction Y/N')
if cont == 'N' or cont == 'n':
break
elif choice == '2':
amount = int(input('Enter the amount to deposit'))
balance = balance + amount
print(f'The Available balance is {balance}')
cont = input('Do you want to do another Transaction Y/N')
if cont == 'N' or cont == 'n':
break
elif choice == '3':
print('The Available balance is',balance)
cont = input('Do you want to do another Transaction Y/N')
if cont == 'N' or cont == 'n':
break
elif choice == '4':
exit()
else:
print('Wrong Choice')

