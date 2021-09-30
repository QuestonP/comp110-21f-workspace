"""My mini game adventure game project"""

from random import randint
__author__ = '730396223'


player: str = ""
DOOR: str = '\U0001f6aa'
points: int = 0
COIN: str = '\U0001fa99'


def greet():
    print("Hello! Welcome to the game! In this game you will be playing through multiple mini games to earn points.")
    global player
    player = input("What would you like to be called? ")


def game_one() -> int:
    """Guess a number mini game"""
    winner: int = randint(0, 25)
    count = 0
    points: int = 0
    while count < 3:
        guess: int = int(input("Enter a number from 1 to 25 "))
        # guess: int = int(input("Guess a number from 1 to 50"))
        if guess == winner:
            points = points + 30
            print(f"You win! Your point total is now {points}")
            return points
        else:
            count = count + 1
            print(f"That was incorrect. You only have {3-count} more tries!")

    if count == 3:
        return points
    return points


def game_two(b: str) -> int:
    """Flip a coin mini game"""
    points: int = 0
    if b == "yes" or "Yes":
        flip: int = randint(1, 2)
        ans: str = ""
        c: int = 0
        while(c < 3):
            your_choice: str = input("Heads or Tails ")
            if flip == 1:
                ans = "heads"
            if flip == 2:
                ans = "tails"
            if your_choice == ans:
                print("Correct! Thats 2 points!")
                points = points + 2
            else:
                print("Incorrect")
            c = c + 1
        print(f"You earned {c} points")
    return points


def game_three() -> int:
    """Guess the country"""
    points: int = 0
    mex: str = "Mexico"
    china: str = "China"
    england: str = "England"
    spain: str = "Spain"
    usa: str = "USA"
    x: int = 1
    while x <= 5:
        question: int = x
        if question == 1:
            print("Hint #1: I am a Spanish speaking dominated country")
            print("Hint #2: I am located in the Americas")
            print("Hint #3: I am the fourth largest country in the Americas")
            if input("What country do you think it is? ") == mex:
                points = points + 10
                print("You are correct! You earned 10 points!")
            else:
                print("Incorrect")
        if question == 2:
            print("Hint #1: I am the most populated country in the world.")
            print("Hint #2: I am located in the eastern hemisphere.")
            print("Hint #3: I house one of the 7 wonders of the world.")
            if input("What country do you think it is? ") == china:
                points = points + 10
                print("You are correct! You earned 10 points!")
            else: 
                print("Incorrect")
        if question == 3:
            print("Hint #1: I am located in western europe.")
            print("Hint #2: The united states was once one of my colonies.")
            print("Hint #3: My flag is blue, red and white.")
            if input("What country do you think it is? ") == england:
                points = points + 10
                print("You are correct! You earned 10 points!")
            else: 
                print("Incorrect")
        if question == 4:
            print("Hint #1: I am a spanish speaking country.")
            print("Hint #2: My capital is Madrid.")
            print("Hint #3: We love soccer here!.")
            if input("What country do you think it is? ") == spain:
                points = points + 10
                print("You are correct! You earned 10 points!")
            else: 
                print("Incorrect")
        if question == 5:
            print("Hint #1: I have arguably the world's strongest military.")
            print("Hint #2: My independence day is July 4th.")
            print("Hint #3: Joe Biden is my president.")
            if input("What country do you think it is? ") == usa:
                points = points + 10
                print("You are correct! You earned 10 points!")
            else: 
                print("Incorrect")
        x = x + 1
        print(f"You earned {points} points this round!")
    return points 


def change_points():
    """Allows the player to ask for points after doing math"""
    name: str = input('Remind me of your name in the game ')
    div: float = len(name)
    if int(input("How many characters are in your game name?")) == div:
        if int(input("What is that number divided by 2 and multipled by 5?")) == div / 2 * 5:
            if int(input("What is that number to multiplied by 3 and divided by 2? ")) == (div / 2 * 5) * 3 / 2:
                global points
                points = points + 50
                print(f"You've earned {points} points!")
    print(f"You got {points} this round")


def free_points(a: int) -> int:
    """Takes players name and sends back points if the number they enter is higher than # of char in player"""
    print(f"Your number is {a}")
    points: int = 0
    add: int = int(input("Enter a number for a chance to earn points! "))
    if len(player) * (a / 2) < a + add:
        points = points + 5
        print("You gained 5 points " + player)
        return points
    else:
        points = points - 5
        print("You lost 5 points " + player)
        return points


def main():
    points = 0
    greet()

    """if statement with 4 doors for each game"""
    print(DOOR + " 1    " + DOOR + " 2    " + DOOR + " 3    " + DOOR + " 4   ")
    path_choice: str = input("Which door do you want to enter? ")

    if path_choice == "1":
        print("You have entered the first door. This door allows you to earn points by guessing the correct number.")
        points = points + game_one()
        if input("BONUS ROUND: Time to earn some xtra points?(Enter the word free)") == "Free" or "free":
            points = points + free_points(randint(0, 15))
    points = points

    if path_choice == "2":
        print("You have entered the second door. This door allows you to gain points by fliping a " + COIN + " guessing what it lands on.")
        points = points + game_two(input("Would you like to play? "))
        if input("BONUS ROUND: Time to earn some xtra points?(Enter the word free)") == "Free" or "free":
            points = points + free_points(randint(0, 15))
    points = points

    if path_choice == "3":
        print("You have entered the third door. This door allows you to obtain points by winning a True or False trivia.")
        points = points + game_three()
        if input("BONUS ROUND: Time to earn some xtra points?(Enter the word free)") == "Free" or "free":
            points = points + free_points(randint(0, 15))
    points = points 

    if path_choice == "4":
        print("You have entered the fourth door.")
        change_points()
        if input("BONUS ROUND: Time to earn some xtra points?(Enter the word free)") == "Free" or "free":
            points = points + free_points(randint(0, 15))
        points = points
    else:
        print("Game over...")

    print(f"You have earned {points} points in the first run of the game!") 

    cont: str = input("Would you like to continue? ")
    if cont != "No" or "no":
        print("Alright then!")
    elif cont == "yes" or "Yes":
        while(cont == "Yes" or "yes"):
            print(DOOR + " 1    " + DOOR + " 2    " + DOOR + " 3    " + DOOR + " 4   ")
            path_choice: str = input("Which door do you want to enter? ")

            if path_choice == "1":
                print("You have entered the first door. This door allows you to earn points by guessing the correct number.")
                points = points + game_one()
                if input("BONUS ROUND: Time to earn some xtra points?(Enter the word free)") == "Free" or "free":
                    points = points + free_points(randint(0, 15))
            points = points

            if path_choice == "2":
                print("You have entered the second door. This door allows you to gain points by fliping a " + COIN + " guessing what it lands on.")
                points = points + game_two(input("Would you like to play? "))
                if input("BONUS ROUND: Time to earn some xtra points?(Enter the word free)") == "Free" or "free":
                    points = points + free_points(randint(0, 15))
            points = points

            if path_choice == "3":
                print("You have entered the third door. This door allows you to obtain points by winning a True or False trivia.")
                points = points + game_three()
                if input("BONUS ROUND: Time to earn some xtra points?(Enter the word free)") == "Free" or "free":
                    points = points + free_points(randint(0, 15))
            points = points 

            if path_choice == "4":
                print("You have entered the fourth door. After a few questions, you can possibly earn points! ")
                change_points()
                if input("BONUS ROUND: Time to earn some xtra points?(Enter the word free)") == "Free" or "free":
                    points = points + free_points(randint(0, 15))
            points = points
    else:
        print("Alright then!")
    print("Game over...")
    print("You have chosen to exit the game.")
    print(f"You have earned {points} points in this run of the game!") 
    print("Thanks for playing " + player + ". Hope you play again!")


if __name__ == "__main__":
    main()
