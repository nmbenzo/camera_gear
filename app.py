from utils import database


USER_CHOICE = """
Please select one of the following:
- 'a' Add a camera and gear
- 's' Show a list of the camera gear you've added
- 'h' Indicate you have a piece camera gear 
- 'r' Remove an item from your inventory 
- 'q' To quit

Your Choice: """


def menu():
    database.create_camera_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_camera()
        elif user_input == 's':
            list_cameras()
        elif user_input == 'h':
            prompt_owned()
        elif user_input == 'r':
            prompt_remove_item()
        else:
            print('Unknown command. Please select a valid input.')

        print('\n')
        menu_again = input('Would you like to see the menu again? (y/n): ')
        if menu_again == 'y':
            user_input = input(USER_CHOICE)
        elif menu_again == 'n':
            break
        else:
            print('Unknown command.')
            user_input = input(USER_CHOICE)


def prompt_add_camera():
    model = input('Please enter a camera: ')
    make = input(f'Which company makes the: {model}: ')
    sensor_size = input(f'What type of sensor: ')
    megapixels = input(f'How many megapixels does the {model} have: ')
    price = input(f'How much does {model} cost?: ')

    database.add_cameras(model, make, sensor_size, megapixels, price)


def list_cameras():
    cameras = database.get_all_cameras()
    for camera in cameras:
        owned = 'YES' if camera['owned'] else 'NO'
        print(f"The {camera['model']} is made by {camera['make']}. Owned: {owned}")
        print(f"It has a(n) {camera['sensor_size']}-sized sensor with "
              f"{camera['megapixels']} megapixels.")


def prompt_owned():
    name = input('Please enter a camera you recently bought: ')

    database.gear_bought(name)


def prompt_remove_item():
    name = input('Please enter camera you recently sold: ')

    database.remove_item(name)


menu()
