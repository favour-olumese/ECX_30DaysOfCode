# ECX 30 Days of Code and Design
Engineering Career Expo, University of Lagos, 30 Days of Code and Design.
### Day 1
#### List to Set
Create a function that takes in a list as input, and returns(and prints) a new list with all repetitions reduced to one appearance alone, as output.
E.g: f(["a", "b", "a", "a", 3, 3, 2, "hello", "b"] ) => ["a", "b", 3, 2, "hello"]. #output

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay1#main.py)  
[Read article](https://thecodingprocess.hashnode.dev/creating-a-new-list-with-multiple-occurrences-removed-using-the-set-function-in-python)

### Day 2
#### Find the mode

Extend the function from day 1, to also print out the modal element(s) of the input list.  i.e, to determine which element occurs the most. If there are multiple such elements, then return a list containing them all.
E.g.: the modal element of the above list is ["a"]

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay2)  
[Read article](https://thecodingprocess.hashnode.dev/finding-the-mode-of-list-items-using-the-multimode-function-in-python)

### Day 3
#### Palindromic numbers
A palindrome is a word that reads the same way forwards and backwards (e.g. Tenet, 101101).
Write a function that prints out all Palindromic numbers less than a given input, and returns the total number of palindromes found.
E.g.: f(500) would print all Palindromic numbers less than 500, as well as the total number of palindromes less than 500.

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay3#main.py)  
[Read article](https://thecodingprocess.hashnode.dev/finding-palindromes-using-python)

### Day 4
#### Decimal to Hexadecimal.
Without using the inbuilt hex() function, write a function that takes an integer as input, and prints out its conversion to Hexadecimal as output.

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay4#main.py)  
[Read article](https://thecodingprocess.hashnode.dev/converting-decimal-to-hexadecimal-without-the-hex-function-in-python)

### Day 5
#### Fibonacci 
Using recursion, write a function that prints out the first "n" members of the Fibonacci series. (The Fibonacci series is a series of integers, starting from 0 and 1, for which each term is the sum of the two preceding term; i.e  [0, 1, 1, 2, 3, 5, 8, 13, 21,...] or "fib(n+1) = fib(n)+ fib(n-1)."

[Execute code](https://replit.com/@favourolumese/Fibonacci-Sequence-Using-Recursion-in-Python?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/fibonacci-sequence-using-recursion-in-python)

### Day 6
#### Man in the well.
A man is stuck at the bottom of a well. Each day, he climbs up 8 metres, and then at night, he slips downwards by 3 metres. Using loops(any loop of your choice), write a function to determine(and print!) how many days it takes for him to climb out of a well of any given depth, where the depth of the well is taken as input.

E.g.: f(17) => the well is 17 metres deep.

**Day 1**: climbs 8m, height = 8m; slips 3m, height=8-3=5m;

**Day 2**: climbs 8m, height = 5 + 8 = 13m; slips 3m, height= 13-3=10m

**Day 3**: climbs 8m, height = 10 + 8= 18m.  But 18>17. STOP.(height climbed has exceeded well depth)

Therefore, f(17)=3 days.

[Execute code](https://replit.com/@favourolumese/ECX30DaysOfCodeDay6#main.py)  
[Read article](https://thecodingprocess.hashnode.dev/solving-word-problem-using-python)

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

[Play game](https://replit.com/@favourolumese/Wordle-Game?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/creating-a-wordle-game-using-python)

### Day 8
#### Caesar Cipher
##### Description
A Caesar cipher is an ancient form of encryption. It involved taking a text(a string) as input and encoding it by replacing each letter with the one n-steps next to it in the alphabet. (E.g.; Shifting "Python" by 5, becomes "Udymts." Note that this "shift" wraps around, which is why "y" becomes "d".)

##### Task: 
* Write a function that takes in as parameters, a plaintext (string) to encode, and a shift value, and outputs the encoded value of the string.

* Write another similar function that takes in the encoded string, with a shift_value, and decodes it.

* Finally, write a third function that takes in a text, a shift value, and a third parameter to indicate whether to encode or decode the given text. (I.e., f("string", 5, True/false), and print out the encoded (or decoded) text accordingly.

[Execute code](https://replit.com/@favourolumese/Caesar-Cipher?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/creating-caesar-cipher-using-python)

### Day 9
#### Is Prime

##### Task:
Write a function that takes an integer as input, and determines whether it is a prime number or not.

[Execute code](https://replit.com/@favourolumese/Prime-Number-Checker-Using-Python?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/prime-number-checker-using-python)

### Day 10
#### USSD Bank Service 

##### Task:
Create a mock USSD service that takes users' inputs, and provides appropriate responses.

* Users provide a USSD code as input

* Users can then choose among a list of options (with numbers), whether to check their balance, send money, purchase airtime, etc.

* For check balance, the user is prompted to provide his password (hard-coded by you.). If correct, s/he is shown the balance—also hard-coded.

* For sending money, the user is prompted to choose from a selection of banks, after which he provides an account number, and then an amount to send. And then a password, which if correct, would send the required amount, and deduct it from  the account balance.

* Follow a similar scheme as sending money, for purchasing airtime—except that in this case, the user is ported for a phone number instead.

[Execute code](https://replit.com/@favourolumese/Mock-Bank-USSD-Service?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/creating-a-mock-ussd-service-using-python)

### Day 11
#### Euclid's Algorithm (Greatest Common Divisor)
The GCD (Greatest Common divisor) of two numbers is the largest number by which both are divisible. E.g.; gcd(42, 18) is 6, since 6 is the highest common factor (HCF—same thing as GCD) of 42 and 18.

##### Task:
Write a program that asks the user for two numbers and computes their GCD using Euclid's algorithm. The process is described below:
* First, compute the remainder of dividing the larger number by the smaller one.
* Next, replace the larger number with the smaller number, and the smaller number with the remainder.
* Repeat this process until the smaller number equals zero. The GCD is the last value of the larger number.
See full [details](https://en.m.wikipedia.org/wiki/Euclidean_algorithm)

[Execute code](https://replit.com/@favourolumese/HCF-Finder?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/creating-an-hcf-finder-using-python)

### Day 12
#### Student or Professor

##### Task:
At a certain school, student email addresses end with @student.college.edu, while professor email addresses end with @prof.college.edu. Write a program that first asks the user how many email addresses they will be entering, and then has the user enter those addresses. After all the email addresses are entered, the program should print out a message indicating exactly how many student and professor emails were entered.

[Read article](https://thecodingprocess.hashnode.dev/finding-the-number-of-time-a-pattern-is-inputted-using-python)

##### Using Regex
[Execute code](https://replit.com/@favourolumese/Email-Addresses-Pattern-Counter-Using-Regex?v=1)

##### Using Endswith Method
[Execute code](https://replit.com/@favourolumese/Email-Addresses-Pattern-Counter-Using-Endswith-Method?v=1)

### Day 13
#### What are the Acronyms?

##### Task:
Write a program that does the following:
* Ask the user to enter (input) a sentence containing an acronym or more.
* Print out a list containing all acronyms in the sentence.
For example:
* Input: "I need to get this done ASAP."; Output–> ["ASAP"]
* Input: "SMH. The NPF is really a joke!"; Output–> ["SMH", "NPF"]
* Input: "LOOOL. I thought you were at KFC"; Output–> ["LOOOL", "KFC"]
(**Note:** An "acronym", for our purposes, is defined as any continuous sequence of UPPERCASE LETTERS, not separated by a whitespace or a symbol.)

[Execute code](https://replit.com/@favourolumese/Simple-Acronyms-Finder-Using-Regular-Expressions?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/simple-acronyms-finder-using-regular-expressions)

### Day 14
#### Guess the Number

##### Task:
* You are to ask a user to guess a number between 1 and 50.
* The user has a maximum of 5 tries.
* If the user guesses wrongly, provide an error message indicating whether their guess was above or below the actual number.
* If the user guesses correctly, congratulate them and show the number of attempts they had.
* If the user exhausts all their tries, tell them they have exhausted their tries and end the game.
E.g.:
```text
> enter a number
user: 1
> wrong. the answer is greater than 1
user: 25
> wrong the answer is less than 25
user: 14
> wrong the number is greater than 14
user: 15
> Correct! You got the right answer in 3 tries.
```
[Execute code](https://replit.com/@favourolumese/Number-Guessing-Game?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/creating-a-number-guessing-game-using-python)

### Day 15
#### Magic Square

##### Task:
A magic square is a 3 by 3 grid, such that:
It contains ALL the numbers 1 through 9. The sum of each row, each column, and each diagonal all add up to the same number. In a program, you can simulate a magic square using a two-dimensional list.

* Write a function that accepts a two-dimensional list as input, and determines whether the list is a magic square or not. Test the function in a program.

[Execute code](https://replit.com/@favourolumese/Magic-Square?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/creating-a-magic-square-using-python)

### Day 16
#### When in Rome

##### Task:
* Write a function that takes an integer as input, and returns it's translation to Roman numerals.
* Using the aforementioned function, write a program that takes user input and prints out their Roman numeral form.
This program must include all necessary type checks or Exception handling

[Execute code](https://replit.com/@favourolumese/Integers-to-Roman-Numerals?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/converting-integers-to-roman-numerals-using-python)

### Day 17
#### Pascal triangle

##### Task:
* Write a function that prints out the first "n" rows of Pascal's triangle.
Where "n" is an integer taken as argument of the function.
[See more](https://en.m.wikipedia.org/wiki/Pascal%27s_triangle)

[Execute code](https://replit.com/@favourolumese/Pascals-Triangle?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/pascals-triangle-using-python)

### Day 18
#### Reverse order

##### Task:
Write a function that takes a string as input, and returns a string similar to the input, but with the words in reverse order, and the punctuation marks maintaining their original order.
E.g.:
f("Hello. I'm Edwin A.J, and you?") => "You. and A.J Edwin I'm, Hello?"
f("What time is it? Hammer time.") => "Time Hammer It is? time what."

**Note:** As shown in the example above, the order of the punctuation marks ("?", "," , ".") have not changed. Only the words have.

[Execute code](https://replit.com/@favourolumese/Reversing-Words-Order-with-Punctuations-Order-Unchanged?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/reversing-words-order-with-punctuations-order-unchanged)

### Day 19
#### Day From Date

##### Task:
Write a function that takes in a date as input, and returns what day of the week it is.
* The input date can be in any convenient format(Whether a "ddmmyy" string, a series of integers, etc)
* Your function must work for both future and past dates.
* Exception handling(or Type checking) is necessary.

[Execute code](https://replit.com/@favourolumese/Day-Name-from-a-Given-Date?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/getting-the-day-of-a-date-using-python)

### Day 20
#### Countdown Timer

##### Task:
Write a program that:
* Asks the user to enter a time period in the form of a number with a unit of either seconds, minutes, or hours.
(E.g. "44s", "32m", "10h".)
* The last character of the string entered would be used to determine its unit.
* Counts down from the input value, and prints out the time left on the clock every second.
* When the time is exhausted, makes a beeping sound non-stop until the user exits the app.

[Execute code](https://replit.com/@favourolumese/Countdown-Timer?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/creating-a-countdown-timer-using-python)

### Day 21
#### Frequency Analysis

##### Task:
* Write a function that takes a string as input and:
Returns a dictionary whose keys are the characters found in the text,
and whose values are the number of occurrences of that character in the text.
E.g.: f("It is good!") => {"I": 2, "t": 1, "s": 1, "g":1, "o":2, "d":1, "!":1}
* Write ANOTHER function that takes an input string and returns a dictionary whose keys are the words in the text, and whose values are the respective frequencies of these words.
E.g.: f("It is not good, is it?") => {"It": 2, "is": 2, "not": 1, "good":1}

Note: In both cases, disregard case sensitivity.

[Execute code](https://replit.com/@favourolumese/Counting-the-Occurrences-of-Letters-and-Words-in-a-Sentence?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/counting-the-occurrences-of-letters-and-words-in-a-sentence-using-python)

### Day 22
#### Zodiac

##### Task:
Extend the function from day 19 to return BOTH the day of the week AND the corresponding "Zodiac sign" of the input date. Return value can be a list or ANY convenient structure.  All rules relating to task 19 still apply.

### Day 23
#### Sieve of Eratosthenes

##### Task:
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

Using the Sieve of Eratosthenes (as described above), Write a function that takes in an integer as input, and returns a list containing all primes less than that input number.

[Execute code](https://replit.com/@favourolumese/Sieve-of-Eratosthenes?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/finding-prime-numbers-using-sieve-of-eratosthenes-in-python)

### Day 24
#### Bubble Sort

##### Task:
"Bubble sort" is a basic algorithm for sorting (rearranging in ascending or descending order) elements in a list.
It operates as follows:

* Iterate across a list, element by element.
* Upon encountering any two adjacent elements which are in the "wrong" designated order (ascending or descending),
swap their positions in the list—else, do nothing!
* Do this until your iteration reaches the end of the list.
* Repeat steps 1) through 3) until there are no longer any adjacent elements in the "wrong" order. Then STOP.
(See more at: [Bubble sort](https://en.m.wikipedia.org/wiki/Bubble_sort).)
Write a function that takes in two parameters, one list of alphabets, and one flag designating what order in which to sort. Using the Bubble sort algorithm, have this function return a SORTED version of the input list.

E.g.: f(['x', 'c', 'b', 'v', 'z', 'a'], "descending") => ['a', 'b', 'c', 'v', 'x', 'z' ]

**Note**: Type checking (or Exception Handling) is necessary.  Disregard case-sensitivity.

[Execute code](https://replit.com/@favourolumese/Bubble-Sort?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/bubble-sort-in-python)

### Day 25
#### Binary Search Algorithm

##### Task:
"Binary search" is a basic algorithm, used to find the position of a target value within a SORTED LIST.
(More details can be found here: Binary search)
For today's task, write a function that takes in two parameters: One list of alphabets, and one character to search.
E.G f("x", ['m', 'v', 'x', 'u'])
In your function:
* first check if the input list is sorted, using any method of your preference. (If it's unsorted,
return a warning indicating so, else continue)
* Using the BINARY SEARCH ALGORITHM, find the position of the input character in the sorted list.
* Return the position of the character in the search list.
* If the character is not found, return false.

[Execute code](https://replit.com/@favourolumese/Binary-Search-Algorithm?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/binary-search-algorithm-in-python)

### Day 26
> We rested.

### Day 27
#### Maths Game

##### Task:
Using Python, create a game with the following rules:
* A(randomly generated) basic algebraic expression is displayed onto the screen.( E.G 36×47, or 117 ÷ 9, etc.)
* The user is required to provide an answer to the expression within 10 seconds.
* If the user provides a RIGHT answer, he gains {10×(the number of seconds left)} points
* If the user provides a WRONG answer, or the time elapsed, the player loses a life.
* At the start of the game, the player provides his name, and begins playing with 3 lives.
* The player loses once he has exhausted his 3 lives.

Note: \n
* Only +,-,×,÷ operations are allowed.
* In the case of a division operation, the two numbers generated MUST be divisible.

[Excute code](https://replit.com/@favourolumese/Maths-Game?v=1)  
[Execute Timed Mental Maths Game (Similar but advanced to Maths Game)](https://replit.com/@favourolumese/Timed-Mental-Maths-Game?v=1)  
[Read Timed Mental Maths Game](https://thecodingprocess.hashnode.dev/timed-mental-maths-game)

### Day 28
#### Bulk E-mail

##### Task:
Using the built-in SMTP module, write a function that takes a list of emails as input, and sends each of them an(any) email message.

### Day 29
#### GPA Calculator

##### Task:
Write a function that:
* Takes as parameters, a list of tuples, containing grades and their corresponding units.
(E.g.: [ ("A", 2), ("A",3), ("B", 2) ... etc.])
* Computes and returns the student GPA, based on the values provides.

**Note:** Handle All necessary exceptions and/or edge cases.

[Execute code](https://replit.com/@favourolumese/GPA-Calculator?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/creating-a-gpa-calculator-using-python)

### Day 30
#### Sudoku Solver

##### Task:
* Write a function that takes in a 9×9 array of NUMBERS.
Let this list represent a partially filled grid of numbers (specifically, of integers ranging from 1 to 9, where "0" signifies an empty space in the grid.) as parameters, and returns as a 9×9 array, the solution(s) to it.
If there are no solutions, return False.

##### Exceptions:
* If an empty list or an invalid list (list with numbers outside the 1-9 range, or empty lists, or a list of wrong size,
etc.) is input, it issues a warning.
(**Hint:** Backtracking is one effective method for solving this problem—it is however, not the only method.)
The problem is further explained below:

Given a partially filled 9×9 list, the goal is to assign digits (from 1 to 9) to the empty cells so that every row,
column, and sub grid of size 3×3 contains exactly one instance of the digits from 1 to 9.

[Execute code](https://replit.com/@favourolumese/Sudoku-Solver?v=1)  
[Read article](https://thecodingprocess.hashnode.dev/creating-a-sudoku-solver-using-python)

