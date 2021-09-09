"""Chaellenge Question during Lecture 9/7"""

choice: int = int(input("Enter a #: "))

# Print A if choice <25
# Print B is choice >=25
# Print C if choice > 75
# Print D if choice >=50 and <=75
if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("C")
        else:
            print("D")
