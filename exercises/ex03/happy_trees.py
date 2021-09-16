"""Drawing forests in a loop."""

__author__ = "730396223"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
count: int = int(input("Depth: "))
trees: str = ""

x: int = 1
while(x <= count):
    y: int = 0
    while(y < x):
        trees = trees + TREE
        print(trees)
        y = y + x
    x = x + 1
