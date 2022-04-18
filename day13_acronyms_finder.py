# ECX 30 DAYS OF CODE AND DESIGN
# Day 13

"""
**What are the acronyms?**

Task: \n
Write a program that does the following:
* Ask the user to enter (input) a sentence containing an acronym or more.
* Print out a list containing all acronyms in the sentence.
For example:
* Input: "I need to get this done ASAP."; Output–> ["ASAP"]
* Input: "SMH. The NPF is really a joke!"; Output–> ["SMH", "NPF"]
* Input: "LOOOL. I thought you were at KFC"; Output–> ["LOOOL", "KFC"]
(Note: An "acronym", for our purposes, is defined as any continuous sequence of UPPERCASE LETTERS,
not separated by a whitespace or a symbol.)

"""
import re

user_input = input('Please, input a statement with acronyms (UPPERCASE): ')

acronyms = re.compile(r'[A-Z.]{2,15}')
acronyms_match = acronyms.findall(user_input)

print(acronyms_match)
