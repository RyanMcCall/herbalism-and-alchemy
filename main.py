from time import sleep

def greeting():
    print()
    print('Welcome to Herbalism and Alchemy App!')
    print()
    sleep(1)

def menu():
    print('Menu:')
    print('1: Find Herbs')
    print('2: Identify Herbs')
    print('3: Craft Potions')
    print('4: Exit')
    print()

def find_herbs():
    # Make the roll
    # Declare a region
    # Roll for ingredients

################
# Running Code #
################

# Greet the user
greeting()
# What does the user want to do?
user_choice = '0'
while user_choice != '4':
    menu()
    user_choice = input('What would you like to do? ')
    print()
    # Find Herbs
    find_herbs()
    # Identify Herbs
    # Craft Potion
    # Exit