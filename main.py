from time import sleep
import region_roll_tables


def greeting():
    print()
    print("Welcome to Herbalism and Alchemy App!")
    print()
    sleep(1)


def show_menu():
    print("Menu:")
    print("1: Find Herbs")
    print("2: Identify Herbs")
    print("3: Craft Potions")
    print("4: Exit")
    print()


def show_valid_regions(list_of_regions):
    print()
    print("Valid Regions")
    print("-------------")
    for item in list_of_regions:
        print(item)
    print()


def get_current_region():
    valid_regions = [
        "arctic",
        "coastal",
        "underwater",
        "desert",
        "forest",
        "grasslands",
        "hills",
        "mountain",
        "swamp",
        "underdark",
    ]

    # Loop until valid response
    show_valid_regions(valid_regions)
    region_response = input("What region are you in? ").lower()

    while True:
        if region_response in valid_regions:
            return region_response
        else:
            region_response = input("Invalid response! Please input a valid region: ")


# Find Herbs
def find_herbs():
    # Make the roll
    print("Have the player make an Herbalism check.")
    sleep(1)
    player_search_roll = int(
        input(
            "(D20 + WIS or INT + Prof if profiecient with and using a Herbalism Kit): "
        )
    )
    # Declare a region
    if player_search_roll >= 15:
        print("Success!")
        region = get_current_region()
        print()
        # Roll for ingredients
        found_ingredients = region_roll_tables.run(region)
        print()
        print("You have found:")
        for herb in found_ingredients:
            print(herb.name)
        print()
    else:
        print("Search failed!")
        print()


# Identify Herbs
def identify_herbs():
    pass


# Craft Potion
def craft_potions():
    pass


def execute_user_choice(choice):
    if choice == "1":
        find_herbs()
    elif choice == "2":
        identify_herbs()
    elif choice == "3":
        craft_potions()
    else:
        print("Please input a valid choice")


################
# Running Code #
################

# Greet the user
greeting()
# What does the user want to do?
user_choice = "0"
while user_choice != "4":
    show_menu()
    user_choice = input("What would you like to do? ")
    print()
    if user_choice != "4":
        execute_user_choice(user_choice)
    # Exit the program
