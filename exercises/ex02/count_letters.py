"""Counting letters in a string."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...
letter: str = input("What letter would you like to search for? ")
word: str = input("Enter a word. ")
count: int = 0
index: int = 0
fin_output: str = ""

while index != len(word):
    if word[index] == letter:
        count = count + 1
    index = index + 1
fin_output = str(count)
print("Count: " + fin_output)
