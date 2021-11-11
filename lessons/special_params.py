"""Examples of optional parameters and union type parameters."""
from typing import Union


def hello(name: Union[str, int, float] = "World") -> str: 
    # creates a default parameter that can be changed by entering a parameter in call
    # Once you choose one parameter you must choose a non default one for every param after
    # Applies to constructors and methods as well
    # Union allows for either the choice between two types 
    result: str = "Hello, "
    if isinstance(name, str):
        return result + name
    elif isinstance(name, float):
        return result + "alien from sector " + str(name)
    else:
        return result + "Comp" + str(name)


print(hello("Quest"))
print(hello())
