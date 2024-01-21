import time

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def introduction():
    print_slow("Welcome to the text-based adventure game!")
    print_slow("You find yourself in a mysterious forest. Your goal is to find the magical artifact.")

def make_choice(options):
    print_slow("Choose an action:")
    for i, option in enumerate(options, 1):
        print_slow(f"{i}. {option}")
    
    choice = None
    while choice not in range(1, len(options) + 1):
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Please enter a number from 1 to", len(options))
    
    return choice

def forest_path():
    print_slow("You stand at a crossroads in the forest.")
    print_slow("1. Go left into the dense forest.")
    print_slow("2. Go right along a narrow path.")

    choice = make_choice(["Explore the left part of the forest", "Explore the right part of the forest"])

    if choice == 1:
        print_slow("You head into the dense forest.")
        return "dense_forest"
    else:
        print_slow("You follow the narrow path.")
        return "narrow_path"

def dense_forest():
    print_slow("In the dense forest, you see an old bridge across a river.")
    print_slow("1. Try to cross the bridge.")
    print_slow("2. Go around the bridge and walk along the river.")

    choice = make_choice(["Cross the bridge", "Go around the bridge"])

    if choice == 1:
        print_slow("You decide to cross the bridge.")
        print_slow("The bridge turns out to be fragile, and you fall into the river.")
        return "game_over"
    else:
        print_slow("You walk along the riverbank.")
        return "river_bank"

def narrow_path():
    print_slow("You find a berry bush.")
    print_slow("1. Pick the berries.")
    print_slow("2. Walk past it.")

    choice = make_choice(["Pick the berries", "Walk past it"])

    if choice == 1:
        print_slow("You pick the berries and put them in your bag.")
        return "continue_path"
    else:
        print_slow("You decide not to touch the berries and continue walking.")
        return "continue_path"

def river_bank():
    print_slow("You come across a small boat station.")
    print_slow("1. Take a boat and cross the river.")
    print_slow("2. Walk past it.")

    choice = make_choice(["Take a boat", "Walk past it"])

    if choice == 1:
        print_slow("You take a boat and cross the river.")
        return "cave_entrance"
    else:
        print_slow("You choose not to take the boat and continue walking along the riverbank.")
        return "river_bank_continue"

def continue_path():
    print_slow("You continue walking along the path.")
    return "cave_entrance"

def river_bank_continue():
    print_slow("After some distance, you see an underground entrance to a cave.")
    return "cave_entrance"

def cave_entrance():
    print_slow("You approach the cave entrance.")
    print_slow("1. Enter the cave.")
    print_slow("2. Go back to the forest.")

    choice = make_choice(["Enter the cave", "Go back to the forest"])

    if choice == 1:
        print_slow("You enter the cave and find the magical artifact!")
        return "victory"
    else:
        print_slow("You decide to return to the forest.")
        return "forest_path"

def game_over():
    print_slow("Game Over. Try again!")

def victory():
    print_slow("Congratulations! You found the magical artifact and won the game!")

if __name__ == "__main__":
    introduction()
    current_location = forest_path()

    while current_location not in ["game_over", "victory"]:
        if current_location == "dense_forest":
            current_location = dense_forest()
        elif current_location == "narrow_path":
            current_location = narrow_path()
        elif current_location == "river_bank":
            current_location = river_bank()
        elif current_location == "continue_path":
            current_location = continue_path()
        elif current_location == "river_bank_continue":
            current_location = river_bank_continue()
        elif current_location == "cave_entrance":
            current_location = cave_entrance()

    if current_location == "game_over":
        game_over()
    elif current_location == "victory":
        victory()
