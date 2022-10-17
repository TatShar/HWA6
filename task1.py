from random import randint

#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst=[]
for i in range (10):
    lst.append (randint(1,10))
print (lst)

ls = [lst[i] for i in range(0, len(lst)) if i%2!=0]
print (ls)
