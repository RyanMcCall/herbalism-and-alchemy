from time import sleep

def greeting():
    print()
    print('Welcome to Herbalism and Alchemy App!')
    print()
    sleep(1)

def show_menu():
    print('Menu:')
    print('1: Find Herbs')
    print('2: Identify Herbs')
    print('3: Craft Potions')
    print('4: Exit')
    print()

# Find Herbs
def find_herbs():
    # Make the roll
    print("Have the player make an Herbalism check.")
    sleep(1)
    player_search_roll = input("(D20 + WIS or INT + Prof if profiecient with Herbalism Kit): ")
    # Declare a region
    # Roll for ingredients

# Identify Herbs
def identify_herbs():
    pass

# Craft Potion
def identify_herbs():
    pass

def craft_potions():
    pass

def execute_user_choice(choice):
    if choice == '1':
        find_herbs()
    elif choice == '2':
        identify_herbs()
    elif choice == '3':
        craft_potions()

################
# Running Code #
################

# Greet the user
greeting()
# What does the user want to do?
user_choice = '0'
while user_choice != '4':
    show_menu()
    user_choice = input('What would you like to do? ')
    print()
    execute_user_choice(user_choice)
    # Exit the program