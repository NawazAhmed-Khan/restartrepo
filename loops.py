#
# nt(row+1, end=" ")
#
# for row in range(10):
#  for column in range(10):
#    print('<' if row % 2 == 1 else '>', end='')
#  print()
# for i in range(10,0,-2):
#     for j in range(0,10,2):
#      print(i, end=' ')
#      print(j, end=' ')

#
# sum=0
# for i in range(10):
#    sum=sum+i
#    print(sum, end='  ')

# print(f'[{"Pakistan":<15}]')
# print('Pakistan:^15')
# x=input('Enter the First Name')
# y=input('Enter last Name')
# z= x + ' ' +y
# print('*' * len(z))
# print(z)
# print('*'* len(z))
# a=int(input('Enter the number of rows'))
# b=int(input('Enter the number of columns'))
# for a in range(a):
#      for b in range(b):
#          print('*', end=' ')
#      print()

import datetime

# def calculate_age(birth_date):
#     today = datetime.date.today()
#     age = today.year - birth_date.year
#
#     # Check if birthday has occurred this year
#     if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
#         age -= 1
#
#     return age
#
# # Prompt the user to enter their birth date
# year = int(input("Enter the year of birth (YYYY): "))
# month = int(input("Enter the month of birth (MM): "))
# day = int(input("Enter the day of birth (DD): "))
#
# # Create a date object from the user's input
# birth_date = datetime.date(year, month, day)
#
# # Calculate the age based on the birth date
# age = calculate_age(birth_date)
# # Print the calculated age
# print("Your age is:", age)

# n=6;
# for i in range(n):
#     for j in range(n):
#         print('*', end=" ")
#     print()
# n=6;
# for i in range(n):
#     for j in range(i+1):
#         print('*', end=" ")
#     print()
# n=6;
# for i in range(n):
#     for j in range(i,n):
#         print('*', end=" ")
#     print()
n = 4;
for i in range(n):
    for j in range(i,n):
        print('', end='')
    for j in range(i+1):
        print('*',end='')
    print()
n = 4;
for i in range(n):
    for j in range(i+1):
        print('', end='')
    for j in range(i,n):
        print('*',end='')
    print()