# ECX 30 Days of Code and Design
Engineering Career Expo, University of Lagos, 30 Days of Code and Design.
### Day 1
#### List to Set
Create a function that takes in a list as input, and returns(and prints) a new list with all repetitions reduced to one appearance alone, as output.
E.g: f(["a", "b", "a", "a", 3, 3, 2, "hello", "b"] ) => ["a", "b", 3, 2, "hello"]. #output

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCode#main.py)

### Day 2
#### Find the mode

Extend the function from day 1, to also print out the modal element(s) of the input list.  i.e, to determine which element occurs the most. If there are multiple such elements, then return a list containing them all.
E.g.: the modal element of the above list is ["a"]

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay2#main.py)

### Day 3
#### Palindromic numbers
A palindrome is a word that reads the same way forwards and backwards (e.g. Tenet, 101101).
Write a function that prints out all Palindromic numbers less than a given input, and returns the total number of palindromes found.
E.g.: f(500) would print all Palindromic numbers less than 500, as well as the total number of palindromes less than 500.

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay3#main.py)

### Day 4
#### Decimal to Hexadecimal.
Without using the inbuilt hex() function, write a function that takes an integer as input, and prints out its conversion to Hexadecimal as output.

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay4#main.py)

### Day 5
#### Fibonacci 
Using recursion, write a function that prints out the first "n" members of the Fibonacci series. (The Fibonacci series is a series of integers, starting from 0 and 1, for which each term is the sum of the two preceding term; i.e  [0, 1, 1, 2, 3, 5, 8, 13, 21,...] or "fib(n+1) = fib(n)+ fib(n-1)."

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay5#main.py)

### Day 6
#### Man in the well.
A man is stuck at the bottom of a well. Each day, he climbs up 8 metres, and then at night, he slips downwards by 3 metres. Using loops(any loop of your choice), write a function to determine(and print!) how many days it takes for him to climb out of a well of any given depth, where the depth of the well is taken as input.

E.g.: f(17) => the well is 17 metres deep.

**Day 1**: climbs 8m, height = 8m; slips 3m, height=8-3=5m;

**Day 2**: climbs 8m, height = 5 + 8 = 13m; slips 3m, height= 13-3=10m

**Day 3**: climbs 8m, height = 10 + 8= 18m.  But 18>17. STOP.(height climbed has exceeded well depth)

Therefore, f(17)=3 days.

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay6#main.py)

### Day 7
#### Wordle Game.
##### Description:
Wordle is a single-player game, in which a user is required to guess a 5-letter hidden word in 6 attempts.

* The user makes a first guess.( E.G: "Skate").

* Print out a progress guide, like this "√××√+"

* "√" Indicates that the letter at that position was guessed correctly.

* "+" indicates that the letter at that position is in the hidden word, but in a different position.

* "×" indicates that the letter at that position is wrong, and isn't in the hidden word.

* This process is repeated until the user either guesses the hidden word correctly—in which case, he wins— or exhausts his 6 attempts, thus loses.

* The "hidden word" is generated randomly from a list of 5-letter words hard-coded by you.

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay7#main.py)

### Day 8
#### Caesar Cipher
##### Description
A Caesar cipher is an ancient form of encryption. It involved taking a text(a string) as input and encoding it by replacing each letter with the one n-steps next to it in the alphabet. (E.g.; Shifting "Python" by 5, becomes "Udymts." Note that this "shift" wraps around, which is why "y" becomes "d".)

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay8#main.py)

##### Task: 
* Write a function that takes in as parameters, a plaintext (string) to encode, and a shift value, and outputs the encoded value of the string.

* Write another similar function that takes in the encoded string, with a shift_value, and decodes it.

* Finally, write a third function that takes in a text, a shift value, and a third parameter to indicate whether to encode or decode the given text. (I.e., f("string", 5, True/false), and print out the encoded (or decoded) text accordingly.

[Execute code]()

### Day 9
#### Is Prime

##### Task:
Write a function that takes an integer as input, and determines whether it is a prime number or not.

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay9#main.py)

### Day 10
#### USSD Bank Service 

##### Task:
Create a mock USSD service that takes users' inputs, and provides appropriate responses.

* Users provide a USSD code as input

* Users can then choose among a list of options (with numbers), whether to check their balance, send money, purchase airtime, etc.

* For check balance, the user is prompted to provide his password (hard-coded by you.). If correct, s/he is shown the balance—also hard-coded.

* For sending money, the user is prompted to choose from a selection of banks, after which he provides an account number, and then an amount to send. And then a password, which if correct, would send the required amount, and deduct it from  the account balance.

* Follow a similar scheme as sending money, for purchasing airtime—except that in this case, the user is ported for a phone number instead.

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeAndDesignDay10#main.py)

### Day 11
#### Euclid's Algorithm (Greatest Common Divisor)
The GCD (Greatest Common divisor) of two numbers is the largest number by which both are divisible. E.g.; gcd(42, 18) is 6, since 6 is the highest common factor (HCF—same thing as GCD) of 42 and 18.

##### Task:
Write a program that asks the user for two numbers and computes their GCD using Euclid's algorithm. The process is described below:
* First, compute the remainder of dividing the larger number by the smaller one.
* Next, replace the larger number with the smaller number, and the smaller number with the remainder.
* Repeat this process until the smaller number equals zero. The GCD is the last value of the larger number.
See full [details](https://en.m.wikipedia.org/wiki/Euclidean_algorithm#:~:text=In%20mathematics%2C%20the%20Euclidean%20algorithm,them%20both%20without%20a%20remainder)

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay11#main.py)
