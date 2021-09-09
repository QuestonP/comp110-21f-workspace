"""Repeating a beat in a loop."""

__author__ = "730396223"


# Begin your solution here...
word: str = input("What beat would you like to repeat? ")
num_of_reps: int = int(input("How many times would you like to repeat it? "))
repeat: str = "" 

if num_of_reps <= 0:
    print("No beat...")
else:
    while(num_of_reps > 0):
        repeat = repeat + word + " "
        num_of_reps = num_of_reps - 1
    print(repeat)
