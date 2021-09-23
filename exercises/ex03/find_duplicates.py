"""Finding duplicate letters in a word."""

__author__ = "730396223"


word: str = input("Enter a word ")
dup: bool = False 
let: str = word[len(word) - 1]

i: int = 0
while(i < len(word)):
    i2: int = len(word) - 1
    while(i2 >= 0):
        if(let == word[i2] and i != i2):
            dup = True
        else:
            i2 = i2 - 1

    i = i + 1
    let = word[i]
print(dup)
