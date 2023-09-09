# print('***************************************************')
# print('============>Student Resut Card Report<============')
# print('***************************************************')
# student_record =int(input('How Many Students Records to be Entered '))
# for i in range(student_record):
#  student_name = input('Enter The Student Name ')
#  student_id = int(input('Enter The Student Id '))

#student_data = ['Ahmad','001',[78,89,67,90,56]]mul_student_data = [['Ahmad','001',[78,89,67,90,56]],['Shahid','002',[78,89,67,90,56]]]
student_data = []
student_marks = list(range(5))


no = int(input('Enter the number of students '))
for i in range(no):
 name = input(f'Enter the student {i+1} Name')
 id = input(f'Enter the student {i+1} id')
student_data.append(name)
student_data.append(id)
for j in range(len(student_marks)):
 marks = int(input(f' Enter the subject {j+1} marks'))
student_marks.append(marks)
student_data.append(student_marks)
print(student_data)
