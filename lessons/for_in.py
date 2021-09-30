"""An example of for in syntax"""


names: list[str] = ["Quest", "Quessie", "Quintin", "Quincy"]

i: int = 0
while i < len(names):
    name: str = names[i]
    print(names[i])
    i += 1

# For in example 

for name in names:
    print(name)
