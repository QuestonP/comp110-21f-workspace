"""Finding duplicate letters in a word."""

__author__ = "730396223"


word: str = input("Enter a word ")
dup: bool = False 
count: int = 0
let: str = word[0]

i: int = 0
while(i < len(word)):
    i2: int = 0
    while(i2 < len(word)):
        if(let == word[i2] and i != i2):
            dup = True
        else:
            i2 = i2 + 1
            let = word[i + 1]
    i = i + 1
print(dup)
