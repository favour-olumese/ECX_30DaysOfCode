# ECX 30 DAYS OF CODE AND DESIGN
# Day 23

"""
**Sieve of Eratosthenes**

The sieve of Eratosthenes is an ancient algorithm for finding all primes less than a given value N.
It operates as follows:

1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).

2. Initially, let p equal 2, the smallest prime number.

3. Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list
(these will be 2p, 3p, 4p, ...; the p itself should not be marked).

4. Find the smallest number in the list greater than p that is not marked. If there was no such number, stop.
Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.

5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
See more: [Sieve of Eratosthenes](https://en.m.wikipedia.org/wiki/Sieve_of_Eratosthenes)

Using the Sieve of Eratosthenes (as described above), Write a function that takes in an integer as input,
and returns a list containing all primes less than that input number.
"""


def sieve_of_eratosthenes(user_input):
    """Prints out prime numbers below the argument inputted"""
    list_of_composite = []              # To store composite numbers
    list_of_prime = []                  # To store prime numbers
    
    prime_num = 2                       # Starting from the first prime number
    multiplier = 2                      # To get the multiples of the prime number
    multiples = 0                       # Store the values of multiples of prime numbers

    while prime_num < user_input:
    
        if prime_num in list_of_composite:
            prime_num += 1
            continue

        else:
            list_of_prime.append(prime_num)

            # Finding multiple of prime and storing them in composite list
            while multiples < user_input:
                multiples = prime_num * multiplier

                # Prevent input same number in composite list
                if multiples in list_of_composite:
                    multiplier += 1
                    continue

                # Input multiples of prime not yet in the composite list
                else:
                    list_of_composite.append(multiples)
                multiplier += 1

            # Reverts the multiplier and multiples variable to zero to prime number to a new number
            multiples = 0
            multiplier = 2
    
        prime_num += 1
    print(list_of_prime)


print(' Find Prime Numbers Using Sieve of Eratosthenes '.center(50, '*'))
print('Find the prime numbers below a certain number.')

try:
    user_inputs = int(input('Enter number: '))

    # Function Call
    sieve_of_eratosthenes(user_inputs)
except ValueError:
    print('Invalid input! Enter only integers.')
