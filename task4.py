#4 Задайте список из N элементов, 
# заполненных числами из 
# промежутка [-N, N]. Найдите 
# произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt 
# в одной строке одно число
n = 10
my_list = []
for i in range(-n,n+1):
    my_list.append(i)
print(my_list)
indexes = open('file.txt','r')
mult = 1
for line in indexes:
    print("номера позиций:", line)
    mult = mult * my_list[int(line)]
print("произведение: ", mult)
