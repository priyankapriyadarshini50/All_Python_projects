line = input("Enter numbers in a line -separated by spaces: ")
if line == '':
    print("The line is empty.")
else:
    num_list = line.split()
    total = 0
    try:

        for num in num_list:
            total += float(num)
        print(f" The sum of the line is {total}")
    except ValueError as e:
        print(e)
        print(num, "is not a string")
