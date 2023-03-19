name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You have met a dead end, do you want to go on the left or right?: ").lower()

if answer == "left":
    answer = input(
        "Whoa! there's a river ahead. Type 'Walk' to walk around it or 'Swim' to swim accross it: ").lower()

    # Conditional options
    if answer == "swim":
        print("You swam across and were sadly eaten by the crocodile.")

    elif answer == "walk":
        print("You walked for many miles and ran out of water, you lost")

    else:
        print("Not a valid option, you lost :(")

elif answer == "right":
    answer = input(
        "You came across a bridge, do you want to (cross/go back)? :").lower()
    print("You went back and lost")

    # Conditional options

    if answer == "cross":
        answer = input(
            "You crossed the brigde and met a stranger. Do you talk to them (yes/no)").lower()

        if answer == "yes":
            print("You talked to them and they gave you gold, you win!")

        elif answer == "no":
            print("You ignored them and lost")

        else:
            print("Not a valid option, you lost :(")

    elif answer == "go back":
        print("You went back and lost")

    else:
        print("Not a valid option, you lost :(")

# If an invalid option is selected do this
else:
    print("Not a valid option, you lost")

print("What an awesome adventure you had there",
      name, "do call in again next time!")
