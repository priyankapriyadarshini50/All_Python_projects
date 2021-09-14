def user_input():
    # Initial Variables
    choice = 'WRONG'
    accepted_value = range(0, 10)
    within_range = False

    # Check the input is digit or within the accepted range
    while choice.isdigit() == False or within_range == False:

        choice = input("Enter a number in between (0-10): ")

        if choice.isdigit() == False:
            print("Sorry, that's not a digit!")
        else:
            if int(choice) in accepted_value:
                within_range = True
            else:
                within_range = False
                print("Sorry, The number is not in the range!")

    return int(choice)


print(user_input())
