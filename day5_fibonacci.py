# ECX 30 DAYS OF CODE AND DESIGN
# Day 5

"""
**fibonacci**

Using recursion, write a function that prints out the first "n" numbers of the Fibonacci series.
"""

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print("Fibonacci Series")
num = int(input('Number of Fibonacci series you want: '))

if num <= 0:
    print('Please, enter a positive integer.')
else:
    for i in range(num):
        print(fibo(i))
