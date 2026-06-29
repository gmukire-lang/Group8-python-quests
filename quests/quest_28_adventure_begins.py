def forest():
    choice = input(
        "You are in a forest. Go north to the castle or south to the river? "
    )
    if choice == "north":
        castle()
    else:
        river()


def castle():
    choice = input("You reach the castle. Knock on the door or sneak around? ")
    if choice == "knock":
        print("Ending 1: The king welcomes you as a hero!")
    else:
        print("Ending 2: Guards catch you sneaking. Game over.")


def river():
    print(
        "Ending 3: You cross the river and discover a hidden village. You live peacefully."
    )


forest()
