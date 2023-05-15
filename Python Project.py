def start_adventure():
    print("Welcome to the Immaculate Adventure game!")
    print("You find yourself standing at a fork in the road.")
    print("Which path do you choose?")
    print("1. Left path")
    print("2. Right path")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice. Please try again.")
        start_adventure()


def left_path():
    print("You chose the left path.")
    print("You stumble upon a hidden treasure chest.")
    print("What do you do?")
    print("1. Open the chest")
    print("2. Leave it alone")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("Congratulations! You found a pile of gold coins.")
        print("You win!")
    elif choice == "2":
        print("You decide to leave the chest and continue your journey.")
        print("As you walk away, you hear a faint whisper...")
        print("Game over!")
    else:
        print("Invalid choice. Please try again.")
        left_path()


def right_path():
    print("You chose the right path.")
    print("You come across a dangerous dragon blocking the way.")
    print("What do you do?")
    print("1. Fight the dragon")
    print("2. Run away")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You engage in an epic battle with the dragon.")
        print("Despite your valiant efforts, the dragon is too powerful.")
        print("You are defeated.")
        print("Game over!")
    elif choice == "2":
        print("You wisely choose to run away from the dragon.")
        print("As you escape, you stumble upon a hidden cave.")
        print("What lies inside?")
        print("1. Enter the cave")
        print("2. Keep running")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("You cautiously enter the cave and discover a secret treasure.")
            print("Congratulations! You found the hidden treasure.")
            print("You win!")
        elif choice == "2":
            print("You decide to keep running, leaving the mystery of the cave behind.")
            print("You continue your journey.")
            print("Game over!")
        else:
            print("Invalid choice. Please try again.")
            right_path()
    else:
        print("Invalid choice. Please try again.")
        right_path()

start_adventure()
