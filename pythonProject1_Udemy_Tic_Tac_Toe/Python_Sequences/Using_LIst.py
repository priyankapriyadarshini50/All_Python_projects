def operation_on_list(my_list):
    for i in range(len(my_list)-1):
        if my_list[i] == 3:
            del my_list[i]
    return my_list


# print(operation_on_list([23, 45, 3, 23, 33]))
# print()


# my_list1 = ['Mary', 'had', 'a', 'little', 'lamb']
def my_list(my_list1):
    del my_list1[3]
    my_list1[3] = 'ram'
    return my_list1
#print(my_list(my_list1))
#print()


# var = 1
# def any():
    #print(var + 1, end='')

#any()
#print(var)

