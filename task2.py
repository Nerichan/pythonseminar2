# 2 Напишите программу, которая принимает 
# на вход число N и выдает набор произведений 
# чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input("enter N: "))
collection = list(range(1, n+1))
print(collection)
def fact(n):  # Обычная функция факториала
    n = len(collection)
    pr=1
    a=[]
    for i in range(1,n+1):
        pr=pr*i
        a.append(pr)
        i = i+1
    return a
print(fact(collection))