"""
Task 3
Have the user enter in the following information and 
store it into a dictionary.  Use an appropriate key 
for each element of the dictionary.

first name
last name
student number
birthdate
grade
email

Then create a loop to repeatedly ask the user for a key.
If the key is in the dictionary, display the value.
If the user types in "quit" then stop the loop.
"""

student = {}

student['first name'] = input('enter your first name: ')
student['last name'] = input('enter your last name: ')
student['student number'] = input('enter your student number: ')
student['birthday'] = input('enter your birthday: ')
student['grade'] = input('enter your grade: ')
student['email'] = input('enter your email: ')

while True:
    x = input('enter a key: ')
    if x in student:
        print(student[x])
    if x == 'quit':
        break