"""Program that demonstrates the properties of the operaters in python."""

age: str = str(input("How old are you? "))
height: str = str(input("How tall are you in inches? "))

int_age: int = int(age)
int_height: int = int(height)
modd: int = int_age % int_height
int_div: int = int_age // int_height
reg_div: float = int_age / int_height
exp: int = int_age**int_height

print("Your age: " + age)
print("Your height: " + height)
print(age + " ** " + height + " is " + str(exp))
print(age + " / " + height + " is " + str(reg_div))
print(age + " // " + height + " is " + str(int_div))
print(age + " % " + height + " is " + str(modd))
