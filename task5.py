#5 Реализуйте алгоритм перемешивания списка.
n = 10
my_list = []
for i in range(1,n+1):
    my_list.append(i)
print(my_list)

def list_mix_1(my_list):
    for j in range(-n, 0):
        temporary_index = 0
        temporary_index = my_list[j+2]
        my_list[j+2] = my_list[j]
        my_list[j] = temporary_index
        j = j+1
    return(my_list)

def list_mix_2(my_list):
    for j in range(0, n):
        temporary_index = 0
        temporary_index = my_list[j-2]
        my_list[j-2] = my_list[j]
        my_list[j] = temporary_index
        j = j+1
    return(my_list)

list_mix_1(my_list)
list_mix_2(my_list)
print(my_list)