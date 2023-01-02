#Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# Пример:
#- 6782 -> 23
#- 0,56 -> 11

intial_number = str(input("enter your number: "))
no_comma = intial_number.replace(".", "")
no_comma = list(no_comma)
the_sum = list(map(int, no_comma))
print(sum(the_sum))
