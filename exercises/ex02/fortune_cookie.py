"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730396223"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune1: str = "You will find out some good news today!"
fortune2: str = "This next week will be a great one for you!"
fortune3: str = "Good news is coming to you soon."
fortune4: str = "New beginnings are approaching."

your_number: int = randint(1, 25)
print("Your fortune cookie says...")
print(your_number)

if your_number <= 6:
    print(fortune1)
else:
    if your_number > 6 or your_number < 13:
        print(fortune2)
    else:
        if your_number >= 13 or your_number < 20:
            print(fortune3)
        else:
            print(fortune4)

print("Now go spread positive vibes!")
