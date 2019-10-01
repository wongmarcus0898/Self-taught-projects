import random

def custom():
    minimum_value = int(input("Insert lowest value: "))
    while minimum_value < 0:
        print("The lowest value must be 0 or greater")
        minimum_value = int(input("Insert lowest value: "))

    maximum_value = int(input("Insert highest value: "))
    while maximum_value <= minimum_value:
        print("The highest value must be greater than", minimum_value)
        maximum_value = int(input("Insert highest value: "))

    return minimum_value, maximum_value

def menu():
    print("Welcome to 'Guess The Number' \nDo you want to customise the numbers?" + "(" + '\033[1m' + "y/n" + '\033[0m' + ")")
    game_mode = input()

    while game_mode != "y" or game_mode != "n":
        if game_mode == "y":
            return custom()
        elif game_mode == "n":
            return  0, 10
        else:
            print("Insert 'y' to yes or 'n' to no")
            game_mode = input()

def main():
    minimum_value, maximum_value = menu()

    number = random.randint(minimum_value, maximum_value)

    print("Guess the number between", minimum_value, "and", maximum_value)
    guess = int(input())

    while guess != number:
        if guess > maximum_value or guess < minimum_value:
            print("Number must be between", minimum_value, "and", maximum_value)
        elif guess > number:
            print("Lower")
        else:
            print("Higher")
        guess = int(input())
    print("You have guessed the number!")

main()