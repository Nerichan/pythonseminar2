# 3 Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n = 6
my_list = []
for i in range (1,n+1):
    my_list.append(i)
print("список 6 чисел: ", my_list)
def sequence(x):
    return((1+1/x)**x)
my_list_new = []
for j in range(1,n):
    new_numbers = sequence(my_list[j])
    my_list_new.append(new_numbers)
print("список чисел последовательности (1+1/х)**1: ", my_list_new)
print("сумма элементов списка последовательности: ", sum(my_list_new))
