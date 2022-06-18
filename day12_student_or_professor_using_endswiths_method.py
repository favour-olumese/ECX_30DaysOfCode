# ECX 30 DAYS OF CODE AND DESIGN
# Day 12

"""
**Student or Professor.**

Task: \n
At a certain school, student email addresses end with @student.college.edu, while professor email addresses end with
@prof.college.edu. Write a program that first asks the user how many email addresses they will be entering,
and then has the user enter those addresses. After all the email addresses are entered,
the program should print out a message indicating exactly how many student and professor emails were entered.
"""

# Using endswith() method

print(' Registration Form '.center(40, '*'))
print('Enter the email addresses of your fellow student member(s) and professor(s)')

student_email = 0
prof_email = 0

try:
    num_of_emails = int(input('How many emails are you entering: '))

    for i in range(num_of_emails):
        user_input = input('Email ' + str(i + 1) + ' : ')

        if user_input.endswith('@student.college.edu'):
            student_email = student_email + 1
        elif user_input.endswith('@prof.college.edu'):
            prof_email = prof_email + 1

    print('\nNumber of emails entered: ', num_of_emails)
    print('You inputted ' + str(prof_email) + ' professor(s) emails')
    print('You inputted ' + str(student_email) + ' student(s) emails')

except ValueError:
    print('Invalid input. Enter an integer.')
