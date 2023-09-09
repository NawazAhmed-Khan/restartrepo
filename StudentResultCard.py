student_data = []
student_subjects=list(range(5))
print('**************************************************')
print('>>>>>>>>>>>>>>>>This The Main Menue<<<<<<<<<<<<<<<')
print('**************************************************')
print('************Please Enter The Choice************  ')
print('Enter The Student data------------------------Press  1 ')
print('Print individual Student Result Card----------Press  2  ')
print('Get The Comprehensive Result Summary----------Press  3  ')
option =int(input('\t Enter The Option  '))
if option ==1:
    while True:
        no=int(input('Enter The Number of Students to be Entered  '))
        for i in range(no):
            name=input(f' Enter the Name of The Student {i+1}:')
            id=int(input(f' Enter The Student {i+1} id: '))
            student_data.append(name)
            student_data.append(id)
            for j in range(len(student_subjects)):
                sub_marks=int(input(f'Enter The obtained Marks of {j+1}: '))
                student_subjects.append(sub_marks)
                student_data.append(student_subjects)
        else:
            break
print(student_data)
if option ==2:
    id_result=int(input('Enter The Student Id '))

            # student_data.append(name)
            # student_data.append(id)
            # for j in range(len(student_marks)):
            #     marks=int(input('f\t Enter The Student Marks {j+1} Marks '))
            #     student_marks.append(marks)
            #     student_data.append(student_marks)
            # else:
            #     break




