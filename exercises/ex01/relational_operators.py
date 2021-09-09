"""A program taking input and using them to demonstrate relational operators."""
__author__ = "730396223"

age: str = str(input("How old are you? "))
height: str = str(input("How tall are you in inches? "))

int_age: int = int(age)
int_height: int = int(height)

greater: bool = int_age < int_height
less_equal: bool = int_age >= int_height
equal_to: bool = int_age == int_height
not_equal: bool = int_age != int_height

print("Your age: " + age)
print("Your height: " + height)
print(age + " < " + height + " is " + str(greater))
print(age + " >= " + height + " is " + str(less_equal))
print(age + " == " + height + " is " + str(equal_to))
print(age + " != " + height + " is " + str(not_equal))
