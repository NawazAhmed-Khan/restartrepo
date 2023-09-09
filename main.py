# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # print(f'************* This is my Calculator  ************')
    # num1 = int(input('Enter the Number of your choice '))
    # num2 = int(input('Enter the second Number of your choice '))
    # operator=input('Enter +, -, /, *  ')
    # if operator == '+':
    #     result=num1+num2
    #     print(f'{num1}+{num2} is', result)
    # elif operator == '-':
    #     result=num1-num2
    #     print(f'{num1}+{num2} is' ,result)
    # elif operator == '*':
    #     result=num1*num2
    #     print(f'{num1}*{num2} is ', result)
    # elif operator == '/':
    #     result=num1/num2
    #     print(f'{num1}/{num2} is', result)
    # else:
    #     print('Choose the right function')

        # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# print('\t**********Operators***********')
# x=10
# y=5
# z=x+y
# print(f'{x}+{y}={z}')
# z=x-y
# print(f'{x}-{y}={z}')
# z=x*y
# print(f'{x}*{y}={z}')
# z=x/y
# print(f'{x}/{y}={z}')
# z=x%y
# print(f'{x}modulus{y}={z}')
# z=x**y
# print(f'{x}^{y}={z}')
# z=x>y
# print(f'{x}>{y}={z}')
# z=x<y
# print(f'{x}<{y}={z}')
# z=x==y
# print(f'{x}={y}={z}')
# z=x>=y
# print(f'{x}>={y}={z}')
# z=x<=y
# print(f'{x}<={y}={z}')
# z=x!=y
# print(f'{x}is not equal to {y}={z}')
# z=(x<y)or(x>y)
# print(f'{x}<{y}or{x}is>{y}={z}')
# z=(x<y)and(x>y)
# print(f'{x}<{y}and {x}>{y}={z}')
# print('\t****************** Daily Wages Pay Slip Calculator ***************   ')
# rate_hour=float(input('\tEnter the working rate  per hour in $ '))
# working_hour=float(input('\tEnter the daily working hour '))
# daily_wage=working_hour*rate_hour
# print("\tThe Daily Wage as per rate without taxes are $", daily_wage)
# print('\t**************Full Month Salary Slip*************')
# monthly_working_days=float(input('\tEnter The Full Month Working days '))
# monthly_basic_salary= monthly_working_days*daily_wage
# print("\tThe Monthly Basic Salary without taxes are $", monthly_basic_salary)
# house_rent=(monthly_basic_salary*40)/100
# print('\tThe House Rent is $' , house_rent)
# medical_allownce=(monthly_basic_salary*30)/100
# print('\tTheMedical Allownces are $', medical_allownce)
# gross_salary=monthly_basic_salary+house_rent+medical_allownce
# print('\tThe Monthly Gross Salary Without Taxes are $' , gross_salary)
# taxes=(gross_salary*25)/100
# print('\tTax deductions are $' , taxes)
# net_salary=gross_salary-taxes
# print('\tThe Full Mont Net Salary after Tax deductions are $', net_salary)


# pincode = '1122'
# balance = 10000
# print('*************** Welcome to My Bank ATM ***************')
# while True:
#     pin=input('\t Please Enter The 4 Digit Pin Code  ')
#     pinlength = len(pin)
#     if pinlength !=4 or pin != pincode:
#         print('\tPlease Enter The 4 Digit Right Pin Code Again  ')
#     else:
#         break
#
# while True:
#         print('\t ************** This is The Main Menu ************** ')
#         print('\t 1. Cash Withdrawl ')
#         print('\t 2. Funds Transfer ')
#         print('\t 3. Cash Deposit ')
#         print('\t 4. Balance Inquiry ')
#         print('\t 5.Exit ')
#         option=int(input('\t Please Enter your Choice '))
#         if option == 1:
#             while True:
#                 amount = int(input('\tPlease Enter The Amount: '))
#                 if amount <= balance:
#                     bal = (balance-amount)
#                     print(f'\tYour Remaining Balance is RS {bal}')
#                     break
#                 else:
#                     print('\tEntered Amount is Greater Than The Available Balance')
#                     cont=input('\t Do YOU WANT AN OTHER TRANSACTION Y/N  ')
#                     if cont == 'N' or cont == 'n':
#                      break
#         elif option == 2:
#             while True:
#                 amount = int(input('\tPlease Enter The Amount Rs '))
#                 transaction = int(input('\tPlease Enter The Account Number '))
#                 if amount <= balance:
#                     bal = balance-amount
#                     print('\t The Amount has been Transfered and The Remaining Balance is Rs ', bal)
#                 break
#             else:
#                 print('\t The Entered Amount is Greater Than The Available Balance ')
#             break
#             cont=input('\t DO YOU WANT AN OTHER TRANSACTION  Y/N  ')
#             if cont == 'N' or cont== 'n':
#                 pass
#

# for Loop print 1 to 50 values horizontallly
# for i in range(1,50):
#     print (i, end='  ')
# table Program
# num = int(input('Enter The Number for Table to be Generated' ' '))
# for i in range(1,21):
#   result = num * (i)
# print(f'{num} * {i }= {result}')
#
# Reverse Number printing
# num = int(input('Enter the Number'' '))
# for i in range(num,0,-1):
#     print(i,end=' ')

# Sum printing
# num = int(input('Enter the number'))
# for i in range(1,30):
#     sum = 0
#     x = range(1, 11)
#     print('number generated from range() function', x)
    # sum = 0
    # for i in range(1,11):
    #  sum = sum + i
    # print('sum=',sum)

    # i = 10
    # while(i >= 1):
    #  print(i,end=' ')
    # i -= 1

    # Nested Loop
    # row = int(input('Enter the number of rows '))
    # col = int(input('Enter the number of columns '))
    #
    # for i in range(1, row + 1):
    #     for j in range(1, col + 1):
    #         print(f'a{i}{j}', end=' ')
    # print()
    #
    # numb = int(input('Enter the number'))


# heart = [
#     "  ***   ***  ",
#     " ***** ***** ",
#     "*************",
#     " *********** ",
#     "  *********  ",
#     "   *******   ",
#     "    *****    ",
#     "     ***     ",
#     "      *      "
# ]
#
# for line in heart:
#     print(line)

# ATM machine
balance = 1000  # Initial account balance

# Function to display the main menu
def printCategory(age):
    if age > 18:
        print('Adult')
    elif age > 65:
        print('Senior Citizen')
    else:
        print('Child')

















