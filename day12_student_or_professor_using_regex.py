# ECX 30 DAYS OF CODE
# Day 12

"""
**Student or Professor.**

Task: \n
At a certain school, student email addresses end with @student.college.edu, while professor email addresses end with
@prof.college.edu. Write a program that first asks the user how many email addresses they will be entering,
and then has the user enter those addresses. After all the email addresses are entered,
the program should print out a message indicating exactly how many student and professor emails were entered.
"""

# Using Regular Expressions

import re

print(' Registration Form '.center(40, '*'))
print('Enter the email addresses of your fellow student member(s) and professor(s)')

try:
    email = []                          # List to store user inputs
    compiled_email = ''                 # Variable to store email list converted to string

    num_of_emails = int(input('How many emails are you entering: '))

    for i in range(num_of_emails):
        user_input = input('Email ' + str(i + 1) + ' : ')
        email.append(user_input)        # Add user inputs to list

    compiled_email = ', '.join(email)   # converting list to string, because only allows strings
    # print(compiled_email)

    # Regex match patterns
    student_email_regex = re.compile(r'\w+@student\.college\.edu')
    prof_email_regex = re.compile(r'\w+@prof\.college\.edu')

    student_match = student_email_regex.findall(compiled_email)
    prof_match = prof_email_regex.findall(compiled_email)

    num_of_student_emails = len(student_match)
    num_of_prof_emails = len(prof_match)

    print('\nNumber of emails entered: ', num_of_emails)
    print('You inputted ' + str(num_of_prof_emails) + ' professor(s) emails')
    print('You inputted ' + str(num_of_student_emails) + ' student(s) emails')

except ValueError:
    print('Invalid input. Enter an integer.')
