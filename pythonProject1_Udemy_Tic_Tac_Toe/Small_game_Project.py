# DISPLAY USER INFORMATION
def user_display(game_list):
    print("This is the current list: ")
    print(game_list)


# ACCEPTING USER INPUT (INDEX POSITION)
def position_choice():
    choice = 'wrong'
    within_range = False
    while choice.isdigit() == False or within_range == False:

        choice = input("Please enter a choice (0,1,2): ")

        if choice.isdigit() == False:
            print("Invalid entry!!")
        else:
            if int(choice) in [0, 1, 2]:
                return int(choice)
            else:
                print("Invalid value!!")
                within_range = False


# ACCEPTING USER INPUT AND UPDATE THE GAME LIST
def position_replacement(game_list, position):
    user_str = input("Enter a string: ")
    game_list[position] = user_str
    return game_list


# USER INPUT FOR CONTINUATION OF GAME
def game_continue():
    ans = 'wrong'

    while ans not in ['Y', 'N']:
        ans = input('Do you want to continue the game? (Y/N): ')
        if ans not in ['Y', 'N']:
            print('I do not understand!!')
        else:
            if ans == 'Y':
                return True
            else:
                return False


game_on = True

game_list = [0, 1, 2]

while game_on:
    # Display the game current list
    user_display(game_list)

    # Take the user input(index)
    position = position_choice()

    # Take user input and update the list
    game_list1 = position_replacement(game_list, position)

    # Display the updated list
    user_display(game_list1)

    # Check if the user want to continue the game
    game_on = game_continue()






