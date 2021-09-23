"""An exercise in remainders and boolean logic."""

__author__ = "730396223"


# Begin your solution here...
carolina: str = "CAROLINA"
tar: str = "TAR"
heels: str = "HEELS"

number: int = int(input("Enter an int "))
if(number % 2 == 0 and number % 7 == 0):
    print('tarheels')
else:
    if(number % 2 == 0):
        print('tar')
    else:
        if(number % 7 == 0):
            print('heels')
        else:
            if(number % 2 != 0 or number % 7 != 0):
                print('carolina')
