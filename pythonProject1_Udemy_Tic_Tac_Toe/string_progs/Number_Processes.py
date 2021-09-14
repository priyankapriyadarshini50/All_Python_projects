def summasion(num_list):
    sum = 0
    for num in num_list:
        #print(int(num))
        sum = sum + int(num)
    return sum


user_num = input("Enter a series of numbers with spaces in between them: ")
user_input_list = user_num.split()
print(user_input_list)
print(summasion(user_input_list))

