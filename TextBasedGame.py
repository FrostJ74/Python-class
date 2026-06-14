#James Frost

# def for main menu
def main_menu():
    # print intro
     print("""***Viking Adventure***
     Welcome. You are a viking trying to protect your village.
    There is a Giant terrorizing the village.
    Your must gather all your supplies before facing the Giant.""")

# instructions for the goal of the game and move commands
def show_instructions():
    # print instructions
    print("""Collect 6 items to win the game or be killed by the giant.
    Move commands: go North, go South, go East, go West, Quit.
     Add to Inventory: get 'item name'""")


def move_between_rooms(current_room, move, rooms):
    # move to corresponding room
    current_room = rooms[current_room][move]
    return current_room


def get_item(current_room, move, rooms, inventory):
    # add item to inventory and remove it from the room
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # dictionary of connecting rooms with items
    rooms = {
        'Great Hall': {'South': 'Docks', 'North': 'Riverbank', 'East': 'Forrest', 'West': 'Farmhouse'},
        'Farmhouse': {'East': 'Great Hall', 'item': 'Mead'},
        'Docks': {'North': 'Great Hall', 'East': 'Longboat', 'item': 'Dried Fish'},
        'Longboat': {'West': 'Docks', 'item': 'Shield'},
        'Riverbank': {'South': 'Great Hall', 'East': 'Fjord', 'item': 'Arm Ring'},
        'Fjord': {'West': 'Riverbank', 'item': 'Axe'},
        'Forrest': {'West': 'Great Hall', 'North': 'Cliffs', 'item': 'Sword'},
        'Cliffs': {'South': 'Forrest', 'item': 'Giant'}  # villain
    }
    s = ' '
    # list for storing player inventory
    inventory = []
    # starting room
    current_room = "Great Hall"
    # show the player the main menu
    main_menu()

    while True:
        # what happens when player encounters the 'villain'
        if current_room == 'Cliffs':
            # winning case
            if len(inventory) == 6:
                print('Congratulations you have defeated the giant and saved the village!')
                print('Thank you for playing!')
                break
            # losing case
            else:
                print('\nOh dear! You did not collect all of the items!')
                print('You were killed by the giant! You were squished!')
                print('GAME OVER!!!')
                print('Thank you for playing!')
                break
        # Tell the user their current room, inventory and prompt for a move, ignores case
        print('You are in the ' + current_room)
        print(inventory)
        # tell the user if there is an item in the room
        if current_room != 'Great Hall' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        print('------------------------------')
        move = input('Enter your move: ').title().split()

        # how player moves to new room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue
        # how player gets an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You pick up the {}'.format(rooms[current_room]['item']))
            print('------------------------------')
            get_item(current_room, move, rooms, inventory)
            continue
        # condition to exit the game
        elif move[0] == 'Quit':
            print('\n**Thank you for playing! Goodbye!**')
            break # This will exit the while loop and end the game

        # if the user enters an invalid command
        else:
            print('Invalid move, please try again')
            continue


main()